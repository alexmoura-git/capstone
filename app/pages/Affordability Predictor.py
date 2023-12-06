import streamlit as st
import pandas as pd
import lightgbm as lgb
import joblib

# Load your trained LightGBM model
model = joblib.load('lightgbm_prod_model.pkl')

# Load the dataset for dynamic neighborhood selection
data = pd.read_csv('app/trimmed_listings.csv') 

def one_hot_encode(df, column_name):
    return pd.get_dummies(df, columns=[column_name], prefix=[column_name], drop_first=True)


# # Function to get neighborhoods based on selected city
def get_neighborhoods(city):
    return data[data['city'] == city]['neighbourhood_cleansed'].unique()

# Streamlit webpage layout
st.title('Airbnb Listing Price Prediction')

# Dropdown for city selection
city = st.sidebar.selectbox('City', data['city'].unique())

# Dynamic dropdown for neighborhood based on selected city
neighborhood = st.sidebar.selectbox('Neighbourhood', get_neighborhoods(city))

# Other input fields
property_type = st.sidebar.selectbox('Property Type', data['property_type'].unique())
room_type = st.sidebar.selectbox('Room Type', data['room_type'].unique())
accommodates = st.sidebar.slider('Accommodates', 1, 10, 2)  # Adjust the range as needed
bathrooms = st.sidebar.number_input('Bathrooms', min_value=1.0, max_value=10.0, value=1.0)
bedrooms = st.sidebar.slider('Bedrooms', 1, 5, 1)  # Adjust the range as needed
beds = st.sidebar.slider('Beds', 1, 5, 1)  # Adjust the range as needed

# Button to make prediction
if st.sidebar.button('Predict Price'):
    # Create a DataFrame from the input features
    input_data = pd.DataFrame([[neighborhood, property_type, room_type, accommodates, bathrooms, bedrooms, beds, city]],
                              columns=['neighbourhood_cleansed', 'property_type', 'room_type', 'accommodates', 'bathrooms_text', 'bedrooms', 'beds', 'city'])
    
    # Preprocess input_data as required by your model
    input_df = pd.DataFrame([input_data])

    for column_name in ['room_type', 'neighbourhood_cleansed', 'city', 'property_type']:
    input_df = one_hot_encode(input_df, column_name)

    # Get the prediction
    prediction = model.predict(input_df)
    
    # Display the prediction
    st.write(f'Predicted Price: ${prediction[0]:.2f}')

# Run the Streamlit app
# To start the app, run `streamlit run app.py` in your terminal
