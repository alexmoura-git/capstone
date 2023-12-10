import streamlit as st
import pandas as pd
import lightgbm as lgb
import joblib

st.image("app/banner.png", width=700)

# Load trained model
model = joblib.load('lightgbm_prod_model.pkl')

# Load the dataset f
data = pd.read_csv('app/trimmed_listings.csv') 

def one_hot_encode(df, column_name):
    return pd.get_dummies(df, columns=[column_name], prefix=[column_name], drop_first=True)


# # Function to get neighborhoods 
def get_neighborhoods(city):
    return data[data['city'] == city]['neighbourhood_cleansed'].unique()

# Title
st.title('Airbnb Listing Price Prediction')

# Dropdown for city 
city = st.sidebar.selectbox('City', data['city'].unique())

# Dynamic dropdown for neighborhood 
neighborhood = st.sidebar.selectbox('Neighbourhood', get_neighborhoods(city))

# Other input fields
property_type = st.sidebar.selectbox('Property Type', data['property_type'].unique())
room_type = st.sidebar.selectbox('Room Type', data['room_type'].unique())
accommodates = st.sidebar.slider('Accommodates', 1, 10, 2)  # Adjust the range as needed
bathrooms = st.sidebar.selectbox('Bathrooms', [1,1.5,2,2.5,3.5,4,4.5,5, 5.5, 6 ,6.5,7])
bedrooms = st.sidebar.slider('Bedrooms', 1, 5, 1)  # Adjust the range as needed
beds = st.sidebar.slider('Beds', 1, 5, 1)  # Adjust the range as needed

def make_prediction(neighborhood, 
                    property_type, 
                    room_type, 
                    accommodates, 
                    bathrooms, 
                    bedrooms, 
                    beds, 
                    city):

    input_data = pd.DataFrame([[neighborhood, property_type, room_type, accommodates, bathrooms, bedrooms, beds, city]],
                                columns=['neighbourhood_cleansed', 
                                'property_type', 
                                'room_type', 
                                'accommodates',
                                'bathrooms_text', 
                                'bedrooms', 
                                'beds', 
                                'city'])


    input_data_encoded=pd.get_dummies(input_data, 
                                        columns=['neighbourhood_cleansed', 
                                'property_type', 
                                'room_type',            
                                'city'])





    X_train=pd.read_csv('app/X_train.csv') 

    missing_cols = set(X_train.columns) - set(input_data_encoded.columns)
    for c in missing_cols:
        input_data_encoded[c] = 0
    input_data_encoded = input_data_encoded[X_train.columns]


    scaler = joblib.load('app/scaler.pkl')

    input_data_encoded_scaled = scaler.transform(input_data_encoded)


    # Load your trained LightGBM model
    model = joblib.load('lightgbm_prod_model.pkl')

    prediction = model.predict(input_data_encoded_scaled)

    return prediction 


# Prediction Buttom
if st.sidebar.button('Predict Price'):


    # Get the prediction
    prediction = make_prediction(neighborhood, 
                    property_type, 
                    room_type, 
                    accommodates, 
                    bathrooms, 
                    bedrooms, 
                    beds, 
                    city)

    print(prediction)
    
    # Display the prediction
    st.write(f'Predicted Price: ${prediction[0]:.2f}')

