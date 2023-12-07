
from config import *
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

import re
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import os
import psycopg2
from sqlalchemy import create_engine, inspect
import seaborn as sns
import matplotlib.pyplot as plt

import re
import warnings
warnings.filterwarnings('ignore')
import tqdm
import random

import datetime
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
pd.set_option('max_rows', 250)
pd.set_option('display.max_colwidth', 1000)









def ingest_data(list_of_cities,list_of_files):


    folder_path = "data"

    df_dic = {}
    geojson_list =[]
    for city in list_of_cities:

        # List all files in the folder
        full_path = folder_path +'/'+ city 
        files = os.listdir(full_path  )
        for file in files:
            if file in list_of_files:
                df=pd.DataFrame()
                if file.endswith(('.gz')):
                    df = pd.read_csv(full_path + '/' + file , compression='gzip')
                elif file.endswith(('.geojson')):
                    with open(os.path.join(full_path, file)) as f:
                        data = json.load(f)
                        geojson_list.append((city,snapshot,file, data))
                elif file.endswith(('.csv')):
                    df = pd.read_csv(full_path + '/' + file )
                df['city'] = city
                df['file']=file

                if file.endswith(('.gz', '.csv')):
                    if file.replace(".",'_') in df_dic:
                        df_dic[file.replace(".",'_')]= pd.concat([df_dic[file.replace(".",'_')],df]) \
                                                         .drop_duplicates()
                    else: 
                        df_dic[file.replace(".",'_')]=df
                    print(full_path + '/' + file)


    # Saving it to pickle as an intermediary step

    for key in df_dic:
            # Shuffle the data
        df_dic[key] = df_dic[key].sample(frac=1).reset_index(drop=True)
        df_dic[key].to_pickle(key + ".pkl")
        print (key, 'Save as pickle')
    
    return



ingest_data(list_of_cities,list_of_files)




listings_csv_gz =pd.read_pickle('listings_csv_gz.pkl')
print(listings_csv_gz.city.unique())

keep_cols = [ 'neighbourhood_cleansed',
             'property_type' , 
             'room_type', 
             'accommodates',
             'bathrooms_text',
             'bedrooms',
             'beds', 
             #'amenities',
             #'review_scores_rating' 
             'review_scores_value',
             'price',  
             'city']

def trim_and_encode_listings(listings_csv_gz, keep_cols ):
    # Fix pricing
    listings_csv_gz.price = listings_csv_gz.price.replace(',','',regex=True
                                                     ).replace('\$','',regex=True).astype('float')



    # Also Trim columns with no reviews to remove inactive properties
    trimmed_listings = listings_csv_gz.dropna(subset=[
                                               'first_review'], how='all', inplace=False)


    # drop rows where bathrooms text, bedrooms or beds are null
    trimmed_listings = trimmed_listings.dropna(subset=[
                                                'bathrooms_text',
                                                'bedrooms',
                                                'beds',
                                                'review_scores_value'],how='any', inplace=False)
    
    trimmed_listings = trimmed_listings[keep_cols]
    
    def extract_numeric_value(series):

        numeric_series = series.apply(lambda x: re.findall(r'\d+\.\d+|\d+', x))
        numeric_series = numeric_series.apply(lambda x: float(x[0]) if len(x) > 0 else 0)
        return numeric_series


    # Get integer in text:    
    trimmed_listings.bathrooms_text =  extract_numeric_value(trimmed_listings.bathrooms_text)

    trimmed_listings = trimmed_listings[trimmed_listings.review_scores_value > 4.5]
    
    trimmed_listings.to_csv('app/trimmed_listings.csv', index=False)
    
    

    
    return trimmed_listings



trimmed_listings = trim_and_encode_listings(listings_csv_gz, keep_cols )


def encoded_listings(df):
    

    def one_hot_encode(df, column_name):
        df_encoded = pd.get_dummies(df, columns=[column_name], prefix=[column_name], drop_first=True)
        return df_encoded

    # one hot encode:
    for column_name in ['room_type', 'neighbourhood_cleansed','city', 'property_type' ]:
        df = one_hot_encode(df, column_name)
    
    df.head().to_csv('app/encoded_listings.csv',index=False)

    return df



def model_grid_search(df, selected_models=None, cv=5, test_size=0.2, n_estimators=[50, 100, 200]):


    # Separate features (X) and target variable (y)
    X = df.drop('price', axis=1)
    y = df['price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    X_train.head().to_csv('app/X_train.csv', index=False)

    # Perform feature scaling
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(scaler, 'app/scaler.pkl')

    # Define the regression models with their parameter grids
    regressors = {
        'Linear Regression': (LinearRegression(), {}),
        'Ridge': (Ridge(), {'alpha': [0.1, 1.0, 10.0]}),
        'Lasso': (Lasso(tol=0.001, max_iter=2000), {'alpha': [0.1, 1.0, 10.0]}),
        'ElasticNet': (ElasticNet(), {'alpha': [0.1, 1.0, 10.0], 'l1_ratio': [0.25, 0.5, 0.75]}),
        'Decision Tree': (DecisionTreeRegressor(), {'max_depth': [None, 5, 10, 20]}),
        'Random Forest': (RandomForestRegressor(), {'n_estimators': n_estimators}),
        'Gradient Boosting': (GradientBoostingRegressor(), {'n_estimators': n_estimators, 'learning_rate': [0.01, 0.1, 1.0]}),
        'XGBoost': (XGBRegressor(), {'n_estimators': n_estimators, 'learning_rate': [0.01, 0.1, 1.0]}),
        'LightGBM': (LGBMRegressor(), {'n_estimators': n_estimators, 'learning_rate': [0.01, 0.1, 1.0]}),
        'k-NN': (KNeighborsRegressor(), {'n_neighbors': [3, 5, 7, 10, 100]}),
        'Neural Network': (MLPRegressor(), {'hidden_layer_sizes': [(100,), (100, 100), (50, 50, 50)]})
    }

    # Train and evaluate each selected regression 
    results = {'RMSE': [], 'R-squared': [], 'Best Parameters': [], 'elapsed_time': []}

    if selected_models is None:
        selected_models = regressors.keys()

    for name in selected_models:
        regressor, param_grid = regressors[name]
        start = datetime.datetime.now()
        print('Starting ', name, ' - ', start)
        grid_search = GridSearchCV(regressor, param_grid, scoring='neg_mean_squared_error', cv=cv)
        grid_search.fit(X_train_scaled, y_train)
        best_estimator = grid_search.best_estimator_
        best_params = grid_search.best_params_
        predictions = best_estimator.predict(X_test_scaled)
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        r2 = r2_score(y_test, predictions)
        results['RMSE'].append(rmse)
        results['R-squared'].append(r2)
        results['Best Parameters'].append(best_params)
        
        end = datetime.datetime.now()
        elapsed_time = end - start
        results['elapsed_time'].append(elapsed_time)
        
        print(name, 'regression complete - ', end, 'elapsed: ', elapsed_time, '-', r2)

        # Save the best performing model
        model_filename = f"{name.lower().replace(' ', '-')}_prod_model.pkl"
        joblib.dump(best_estimator, model_filename)

    # Create table
    results_df = pd.DataFrame(results, index=selected_models)
    
    return results_df









def remove_outliers_and_save_model( high_cut_off, low_cut_off = 10, no_eval = True):
    selected_models = [#'Linear Regression', 'Ridge', 'Lasso', 'ElasticNet', 
                       'LightGBM']
    
    # Filtering out records outside the low and high cut-off range
    filtered_data = trimmed_listings[(trimmed_listings.price >= low_cut_off) & (trimmed_listings.price <= high_cut_off)]
    filtered_data.to_csv('app/filtered_data.csv', index=False)
    
    # Counting excluded records
    excluded = len(trimmed_listings) - len(filtered_data)
    print(excluded, 'records excluded')
    print(len(filtered_data), 'records included')
    
    if no_eval== False:
    # Perform model grid search on the filtered data
        results = model_grid_search(encoded_listings(filtered_data), selected_models=selected_models)

        results['low_cut_off'] = low_cut_off
        results['high_cut_off'] = high_cut_off
        results['excluded'] = excluded
        #results.to_pickle('results_{}_{}.pkl'.format(low_cut_off, high_cut_off))
        
        return_value= results, filtered_data
    
    else:
        return_value=  filtered_data
    
    return return_value

    
remove_outliers_and_save_model (high_cut_off, low_cut_off, no_eval =False )




file_to_remove = 'listings_csv_gz.pkl'
if os.path.exists(file_to_remove):
    os.remove(file_to_remove)
    print(f"{file_to_remove} has been removed.")
else:
    print(f"{file_to_remove} does not exist in the current directory.")