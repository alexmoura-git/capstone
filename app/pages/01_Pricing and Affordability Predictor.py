import streamlit as st
import pandas as pd
import lightgbm as lgb
import joblib
import numpy as np

st.image("app/banner.png", width=700)


import altair as alt
import pandas as pd
import numpy as np


import streamlit as st




## chart ----------------
def affordability_pressure_chart(predicted_rent, median_rent, max_val):
    
    max_val=max(predicted_rent, median_rent, max_val)

    # Create Data Frame with Points
    data = pd.DataFrame({
        'Predicted AirbnB Income': [predicted_rent],
        'Neigboorhood Median Rent': [median_rent]
    })

    if predicted_rent > median_rent: 
        icon_text = '🏠 ⚠️ '
    else:
        icon_text = '🏠'

    # Base chart 
    points = alt.Chart(data).mark_text(
        text=icon_text , 
        fontSize=30,
        align='center'
    ).encode(
        x='Predicted AirbnB Income:Q',
        y='Neigboorhood Median Rent:Q'
    )


    # Create a DataFrame for the 45-degree line
    line_data = pd.DataFrame({'x': np.linspace(0, max_val, 100)})
    line_data['y'] = line_data['x']

    # Create the area chart
    area_chart = alt.Chart(line_data).mark_area(
        line={'color':'darkred'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='white', offset=0),
                   alt.GradientStop(color='red', offset=1)],
            x1=0,
            x2=1,
            y1=0,
            y2=1
        )
    ).encode(
    x=alt.X('x', axis=alt.Axis(title='Predicted AirbnB Income')),  # Removing x-axis title
    y=alt.Y('y', axis=alt.Axis(title='Neigboorhood Median Rent'))  # Setting y-axis title
)


    text = alt.Chart(pd.DataFrame({'x': [max_val * 0.95], 'y': [max_val * 0.05], 'text': ['Affordability Pressure Region']})).mark_text(
        align='right',
        baseline='bottom',
        fontSize=12,
        color='white'
    ).encode(
        x='x:Q',
        y='y:Q',
        text='text:N'
    )


    return_chart = (area_chart + points + text).configure_axis(
        grid=False
    ).properties(
    width=250,
    height=250
)



    return return_chart 

## chart ----------------




# Load trained model
model = joblib.load('lightgbm_prod_model.pkl')

# Load the dataset f
data = pd.read_csv('app/trimmed_listings.csv') 

def one_hot_encode(df, column_name):
    return pd.get_dummies(df, columns=[column_name], prefix=[column_name], drop_first=True)


# # Function to get neighborhoods 
def get_neighborhoods(city):
    return data[data['city'] == city]['neighbourhood_cleansed'].unique()


# # Function to get neighborhoods 
def get_property_type(room_type):
    return data[data['room_type'] == room_type]['property_type'].value_counts().head(5).index

# Title
st.markdown("""**Use panel on the left to calculate estimated rental and affordability**""")


# Dropdown for city 
city = st.sidebar.selectbox('City', np.sort(data['city'].unique()))

# Dynamic dropdown for neighborhood 
neighborhood = st.sidebar.selectbox('Neighbourhood', np.sort(get_neighborhoods(city)))

# Other input fields
room_type = st.sidebar.selectbox('Room Type',  ['Entire home/apt', 'Private room'])
property_type = st.sidebar.selectbox('Property Type', np.sort(get_property_type(room_type)))
accommodates = st.sidebar.slider('Accommodates', 1, 10, 2)  # Adjust the range as needed
bathrooms = st.sidebar.selectbox('Bathrooms', [1,1.5,2,2.5,3.5,4,4.5,5, 5.5, 6 ,6.5,7])
bedrooms = st.sidebar.slider('Bedrooms', 1, 5, 1)  # Adjust the range as needed
#beds = st.sidebar.slider('Beds', 1, 5, 1)  # Adjust the range as needed

def make_prediction(neighborhood, 
                    property_type, 
                    room_type, 
                    accommodates, 
                    bathrooms, 
                    bedrooms, 
                 #   beds, 
                    city):

    input_data = pd.DataFrame([[neighborhood, property_type, room_type, accommodates, bathrooms, bedrooms, 
                               # beds, 
                                city]],
                                columns=['neighbourhood_cleansed', 
                                'property_type', 
                                'room_type', 
                                'accommodates',
                                'bathrooms_text', 
                                'bedrooms', 
                                #'beds', 
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


uszip_stats=pd.read_csv('app/uszip_stats.csv')
def get_median_rent(city, neighborhood):
    filtered_data = uszip_stats[(uszip_stats['city'] == city) & (uszip_stats['neighbourhood_cleansed'] == neighborhood)]
    median_rent = filtered_data['rent_median'].median()
    return median_rent

median_rent= get_median_rent(city, neighborhood)


# Prediction Buttom
if st.sidebar.button('PREDICT'):

    st.markdown("""--- """)
    # Get the prediction
    prediction = make_prediction(neighborhood, 
                    property_type, 
                    room_type, 
                    accommodates, 
                    bathrooms, 
                    bedrooms, 
                   # beds, 
                    city)

    print(prediction)
    

    


    days_in_month = 30
    airbnb_fee = 0.16
    additional_expenses = 0.10
    occupancy_rate = 0.564
    medium_neiboorhood_rental = 200
    predicted_monthly_income = prediction[0] * days_in_month * occupancy_rate * (1 - airbnb_fee - additional_expenses)

    # Display the prediction

    st.write(f'The Median Rent income in **{neighborhood} - {city}** is  **\${median_rent:.2f}**. The Predicted Income for this AirBnB property is  **\${predicted_monthly_income:.2f}**')
    if predicted_monthly_income>median_rent:
        message = "Given that investors may earn more by turning this property in a short-term rental, investing or staying in this property may be increasing the price pressure in the local rental market. The red region in the chart below shows the area in which property income are more liklely to be competing with local housing."
        st.markdown(f'<span style="color:red">{message}</span>', unsafe_allow_html=True)
    else:
        message = "Median Rent is still higher than the expected monthly income for this AirBnB property, which makes unlikely that this rental is putting pressure in the local rental prices. The red region in the chart below shows the area in which property income are more liklely to be competing with local housing."
        st.markdown(f'<span style="color:green">{message}</span>', unsafe_allow_html=True)


    chart = affordability_pressure_chart(predicted_monthly_income , median_rent,5000)

    st.altair_chart(chart, use_container_width=True)

    st.markdown('---')
    # Markdown table
    
    markdown_table =f"""

    **Methodology, Calculation and Assumptions:**
    1. We created a machine learning model from AirBnB listings using the data available at [Inside Airbnb](http://insideairbnb.com/get-the-data). The daily rental predictions on this page are based on this model.
    2. Based on the predicted daily rental we canclculate the net predicted monthly rental as per table below:

    | Description                          | Value |
    |--------------------------------------|---------------|
    | Predicted Daily Rental               | ${prediction[0]:.2f} |
    | Number of days in a month            | {days_in_month} |
    | [Airbnb host only fee](https://www.airbnb.com/help/article/1857)        | {airbnb_fee:.2%}|
    | Additional Airbnb expenses - Sheets, Laundry, Wear and Tear | {additional_expenses :.2%}|
    | Occupancy rate (assumption from [Airdna](https://www.airdna.co/blog/2023-us-short-term-rental-outlook-report) | {occupancy_rate:.2%}|
    | **Net Predicted Monthly Rental Income** |**${predicted_monthly_income :,.2f}**|

    
    **Predicted Monthly Rental Income**: \`daily_rental * number_of_days * occupancy_rate * (1 -aibnb_fee)\`

    3. In order to build the plot we assumed that whenever the predicted net monthly income for short term rental is higher than the average rental income, there is an incentive for the owner to flip the property to short term rental. 
   
    In practice many other factors should be considered as investor/onwer prefferences, additional expenses related to each rental mode or local/property restructions such as community bylaws.
    
    Our predictor tool was created as part of an academic project and in line with the mission of the InsideAirbnB website which served as our main data source. Use your own analysis and judment before using the information provided by the tool for investment of travel lodging decisions
    """

    st.markdown(markdown_table)

