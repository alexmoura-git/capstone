import pandas as pd
import numpy as np
from uszipcode import SearchEngine
import urllib.parse
import geopandas as gpd
from geojson import Point, Polygon, Feature, MultiPolygon
from shapely.geometry import Polygon, Point, shape
from tqdm import tqdm
import os
from collections import Counter
import json

#Import USZips and Clean
us_zip_read_file_path = 'app/choropleth/data/source data/uszips.csv'

us_df = pd.read_csv(us_zip_read_file_path)

#drop zips with na value
us_df.dropna(subset=['zip'], inplace=True)

## Transform zip column to string to include 0 and 00 in number
def transform_zip_columnt(df):
    df['zip'] = df['zip'].astype(str)
    zip_codes = df['zip']
    updated_codes = []
    
    for zip_code in zip_codes:
        if len(zip_code) == 3:
            new_code = "00"+zip_code
            updated_codes.append(new_code)
        elif len(zip_code) == 4:
            new_code = "0"+zip_code
            updated_codes.append(new_code)
        else:
            updated_codes.append(zip_code)
            
    df['zip'] = updated_codes
    
    return df


us_df_transformed = transform_zip_columnt(us_df)

# Get neighborhood for zip/lat,lon
# NEED TO LOCALLY RUN THE IMPORT AIRBNB SCRIPT to RUN THIS
def get_df_all_neighborhood(geojson_file, dataframe):
    gdf = gpd.read_file(geojson_file)
    neighborhoods_mapping = {}  

    for i, (lat, lon) in enumerate(zip(list(dataframe.lat), list(dataframe.lng))):
        point = Point(lon, lat) 
        found = False

        # Create a Counter to count occurrences of neighborhoods for selected lat lon
        neighborhoods_counter = Counter()

        for index, row in gdf.iterrows():
            neighborhood_name = row['neighbourhood']
            neighborhood_geometry = row['geometry']

            # Check for validity before performing search
            if neighborhood_geometry.is_valid and point.is_valid:
                buffered_point = point.buffer(1e-9)  # Add buffer to get more precise location

                if neighborhood_geometry.contains(buffered_point):
                    neighborhoods_counter[neighborhood_name] += 1
                    found = True

        # Choose the neighborhood based on occurrences or take the first one if there are no multiple occurences
        if found:
            chosen_neighborhood = neighborhoods_counter.most_common(1)[0][0]
            neighborhoods_mapping[i] = chosen_neighborhood
        else:
            neighborhoods_mapping[i] = np.nan  

    dataframe['neighborhood'] = dataframe.index.map(neighborhoods_mapping)

    return dataframe

# Get list of geojsons
def list_files_data_directory(directory, suffix):
    city_file_pairs = []
    for root, dirs, files in os.walk(directory):
        # exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            # exclude hidden files
            if not file.startswith('.'):
                if file.endswith(suffix):
                    city = os.path.basename(root)
                    city_file_pairs.append((os.path.join(root, file), city))
    return city_file_pairs

# getlist of files
geojson_files = list_files_data_directory('app/data/geojsons','neighbourhoods.geojson')

new_dir = 'app/choropleth/data/transformed/neighborhood_mapped'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    
# Write dataframes with neighborhoods to folders
for file, file_name in tqdm(geojson_files, desc='Processing files', unit='file'):
    us_neighborhoods_df = get_df_all_neighborhood(file, us_df_transformed)
    write_file_path = os.path.join(new_dir, file_name + '_neighborhood_df.csv')

    # Write the DataFrame to a csv file
    us_neighborhoods_df.to_csv(write_file_path)

#Import HUD Data
hud_df = pd.read_excel('app/choropleth/data/source data/Zipcode_2022_2020census.xlsx')
hud_df.rename(columns={'code':'zip'}, inplace=True)

#Transform zip
hud_df_transformed = transform_zip_columnt(hud_df)
hud_df_transformed = hud_df_transformed.loc[hud_df_transformed['program_label'] == 'Summary of All HUD Programs']
hud_df_transformed = hud_df_transformed[['zip', 'total_units', 'rent_per_month', 'hh_income', 'person_income']]

# Merge HUD and US Data and Aggregate Neighborhood Data
# Create a new folderfor data and see if this pushes correctly
new_dir = 'choropleth/data/final/'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# Get choropleth_data
def list_files_trimmed(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and not f.startswith('.')]
    city_file_pairs = [(f, f.split('_neighborhood_df.csv')[0]) for f in files]
    return city_file_pairs

transformed_files = list_files_trimmed('choropleth/data/transformed/neighborhood_mapped')


agg_us_neighborhoods_df = pd.DataFrame(columns=['neighborhood','city','population','density',
                                             'family_size','income_household_median','income_individual_median',
                                             'home_ownership', 'housing_units','home_value','rent_median',
                                             'rent_burden', 'labor_force_participation','unemployment_rate',
                                             'poverty', 'total_units', 'rent_per_month','hh_income'])


for file, city in transformed_files:
    us_neighborhoods_df = pd.read_csv('app/choropleth/data/transformed/neighborhood_mapped/'+file)
    us_neighborhoods_df = transform_zip_columnt(us_neighborhoods_df)
    us_neighborhoods_df = us_neighborhoods_df[['zip','neighborhood','city','population','density', 'family_size','income_household_median','income_individual_median','home_ownership', 'housing_units','home_value','rent_median','rent_burden', 'labor_force_participation','unemployment_rate','poverty']]
    neighborhoods_df = pd.merge(us_neighborhoods_df, hud_df_transformed, on=['zip'])
    neighborhoods_df['city'] = city
    neighborhoods_df.dropna(subset = ['neighborhood'], inplace=True)
    #neighborhoods_df['zip'] = neighborhoods_df['zip'].astype(int)
    
    agg_neighborhoods_df = neighborhoods_df.groupby(['neighborhood','city']).agg({
        'population': 'sum',
        'density': 'mean',
        'family_size': 'sum',
        'income_household_median': 'mean',
        'income_individual_median': 'mean',
        'home_ownership': 'mean',
        'housing_units': 'sum',
        'home_value': 'sum',
        'rent_median': 'mean',
        'rent_burden': 'mean',
        'labor_force_participation': 'mean',
        'unemployment_rate': 'mean',
        'poverty': 'mean',
        'total_units': 'sum',
        'rent_per_month': 'mean'
    }).reset_index()
    
    agg_us_neighborhoods_df = pd.concat([agg_us_neighborhoods_df, agg_neighborhoods_df], ignore_index=True)
    
# Aggregate and add listing data
# NEED TO RUN ALEX'S IMPORT AIRBNB TO GENERATE
listing_files = list_files_data_directory('app/data/trimmed','listings.csv.gz')

listing_df = pd.DataFrame(columns = ['city','neighborhood','price'])

for file, city in listing_files:
    df_lis = pd.read_csv(file)
    df_lis['city'] = city
    df_lis['price'] = df_lis['price'].replace(',','',regex=True).replace('\$','',regex=True).astype('float')
    df_lis.rename(columns={'neighbourhood_cleansed': 'neighborhood'}, inplace=True)
    df_lis = df_lis[['city','neighborhood','price']]
    listing_df = pd.concat([listing_df, df_lis], ignore_index=True)
    
agg_listing_df = listing_df.groupby(['neighborhood','city']).agg({
        'price': 'mean'
    }).reset_index()

agg_neighborhoods_df = pd.merge(agg_us_neighborhoods_df, agg_listing_df, on=['city', 'neighborhood'])

write_file_path = os.path.join(new_dir, 'agg_us_neighborhood_df.csv')

    # Write the df to a csv file
agg_neighborhoods_df.to_csv(write_file_path)