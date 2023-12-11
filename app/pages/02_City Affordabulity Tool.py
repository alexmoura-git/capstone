import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import json
import os
import ast

# Set page title and icon
st.set_page_config(page_title="Impact of Airbnb on housing affordability", page_icon="🏡")

st.image("app/banner.png", width=700)

## Import DF
df = pd.read_csv('capstone/app/choropleth/data/final/agg_us_neighborhood_df.csv')

def remove_decimal(value):
    try:
        numeric_value = float(value)
        if numeric_value.is_integer():
            return str(int(numeric_value))
    except (ValueError, TypeError):
        pass  

    return value

df['neighborhood'] = df['neighborhood'].apply(remove_decimal)

## Function to get cities 
def get_cities(df):
    return df['city'].unique().tolist()

## Function to get neighborhoods 
def get_neighborhoods(df, city):
    return df[df['city'] == city]['neighborhood'].unique().tolist()


## FUnction to generate choropleth
def choropleth(city, choro_neighborhood, agg_neighborhoods_df, metric_option):
    # Get GeoJson File and format
    geo_json_file_path = city_file_path = os.path.join('data', city, 'neighbourhoods.geojson')
    geo_json = json.load(open(geo_json_file_path))
    
    #Create rental multipliers
    agg_neighborhoods_df['Affordable Rent to Affordable Income'] = round(agg_neighborhoods_df['rent_per_month']/((agg_neighborhoods_df['income_household_median']*.5)/12))
    agg_neighborhoods_df['Median Rent to Affordable Income'] = round((agg_neighborhoods_df['rent_median']/((agg_neighborhoods_df['income_household_median']*.5)/12)))
    agg_neighborhoods_df['Short-Term Rent to Affordable Income'] = round((agg_neighborhoods_df['price']*30*.564)/((agg_neighborhoods_df['income_household_median']*.5)/12))

    agg_neighborhoods_df_city = agg_neighborhoods_df[agg_neighborhoods_df.city == city]
    

    # Get Lat Lons for City Center
    list_of_cities_lat_lon = sorted([('columbus', 39.9612, -82.9988, 8.75),
                                      ('los-angeles', 34.0549, -118.2426, 7.25),
                                      ('new-york-city', 40.7128, -74.0060, 8.25),
                                      ('fort-worth', 32.7555, -97.3308, 8.25),
                                      ('boston', 42.3601, -71.0589, 9.25),
                                      ('broward-county', 26.1224, -80.1373, 8.25),
                                      ('chicago', 41.8781, -87.6232, 8.25),
                                      ('austin', 30.2672, -97.7431, 8.5),
                                      ('seattle', 47.6061, -122.3328, 9.25),
                                      ('rochester', 43.1566, -77.6088, 9.25),
                                      ('san-francisco', 37.7749, -122.4194, 9.25),
                                      ('asheville', 35.5951, -82.5515, 8.5),
                                      ('cambridge', 42.3736, -71.1097, 10),
                                      ('clark-county', 36.079561, -115.094045, 6.5),
                                      ('dallas', 32.7767, -96.7970, 8.5),
                                      ('denver', 39.7392, -104.9903, 9.25),
                                      ('hawaii', 21.3099, -157.8581, 5),
                                      ('jersey-city', 40.7178, -74.0431, 9.25),
                                      ('nashville', 36.1638, -86.7819, 8.5),
                                      ('new-orleans', 29.9511, -90.0715, 8.5),
                                      ('oakland', 37.8035, -122.2716, 9.25),
                                      ('pacific-grove', 36.6177, -121.9166, 9.25),
                                      ('portland', 45.5173, -122.6836, 9.25),
                                      ('salem', 44.9429, -123.0351, 9.25),
                                      ('san-diego', 32.7167, -117.1661, 8.25),
                                      ('san-mateo-county', 37.5630, -122.3255, 9.),
                                      ('santa-cruz-county', 36.9752, -121.9533, 9.25),
                                      ('twin-cities', 44.9778, -93.2650, 6.5),
                                      ('washington-dc', 38.9072, -77.0369, 9.5)
                                      ])


    # Get matching city from list_of_cities for map location and zoom
    matching_lat_lon = None

    for city_lat_lon in list_of_cities_lat_lon:
        if city_lat_lon[0] == city:
            matching_lat_lon = city_lat_lon
            break  

    city_center_lat_lons = matching_lat_lon
    city_center_lat = city_center_lat_lons[1]
    city_center_lon = city_center_lat_lons[2]
    city_center_zoom = city_center_lat_lons[3]

    # Selected neighborhood
    pin_point_df = pd.read_csv('choropleth/data/final/pin_point_coordinates.csv')
    pin_point_df['coordinates'] = pin_point_df['coordinates'].apply(ast.literal_eval)
    neigh_val = pin_point_df.coordinates[
        (pin_point_df['city'] == city) & (pin_point_df['neighborhood'] == choro_neighborhood)]
    neigh_lat_lons = neigh_val.values

    ## Generate Figure
    hover_text = choro_neighborhood

    # Location Hover Text
    hover_df = agg_neighborhoods_df_city[agg_neighborhoods_df_city['neighborhood'] == choro_neighborhood]
    for _, row in hover_df[['Affordable Rent to Affordable Income', 'Median Rent to Affordable Income', 'Short-Term Rent to Affordable Income']].iterrows():
        for column in row.index:
            hover_text += f"<br>{column}: {row[column]}"
            
    #Get data to show
    if metric_option == 'Affordable Rent to Affordable Income':
        color_value = 'Affordable Rent to Affordable Income'
        range_color_value = (max(0, agg_neighborhoods_df_city['Affordable Rent to Affordable Income'].min()), agg_neighborhoods_df_city['Affordable Rent to Affordable Income'].max())
    elif metric_option == 'Median Rent to Affordable Income':
        color_value = 'Median Rent to Affordable Income'
        range_color_value = (max(0, agg_neighborhoods_df_city['Median Rent to Affordable Income'].min()), agg_neighborhoods_df_city['Median Rent to Affordable Income'].max())
    elif metric_option == 'Short-Term Rent to Affordable Income':
        color_value = 'Short-Term Rent to Affordable Income'
        range_color_value = (max(0, agg_neighborhoods_df_city['Short-Term Rent to Affordable Income'].min()), agg_neighborhoods_df_city['Short-Term Rent to Affordable Income'].max())

    # Choropleth
    fig = px.choropleth_mapbox(agg_neighborhoods_df_city,
                               geojson=geo_json,
                               locations="neighborhood",
                               featureidkey='properties.neighbourhood',
                               color=color_value,
                               color_continuous_scale=px.colors.sequential.OrRd,
                               range_color=range_color_value,
                               mapbox_style="carto-positron",
                               zoom=city_center_zoom, center={"lat": city_center_lat, "lon": city_center_lon},
                               opacity=0.7,
                               hover_name='neighborhood',
                               hover_data=['Affordable Rent to Affordable Income', 'Median Rent to Affordable Income', 'Short-Term Rent to Affordable Income'],
                               title='Neighborhood Affordability Data'
                               )

    fig.update_layout(dragmode=False)

    # Property Neighborhood Marker
    fig.add_trace(go.Scattermapbox(
        lat=[neigh_lat_lons[0][1]],
        lon=[neigh_lat_lons[0][0]],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=8,
            color='green',
        ),
        text=[hover_text],
        hoverinfo='text'
    ))
    
    # Display the choropleth graph with fixed size
    st.plotly_chart(fig, use_container_width=True, height=1500, width=1500)


# Title
st.markdown('#### Select the City and Neighbourhood to see the percent of household income that would be allocated to rent')

# Dropdown for city 
city = st.sidebar.selectbox('City', np.sort(df['city'].unique()))

# Dynamic dropdown for neighborhood 
neighborhood = st.sidebar.selectbox('Neighbourhood', np.sort(get_neighborhoods(df, city)))

# Other input fields
color_scale = st.sidebar.selectbox('Color Scale',  ['Short-Term Rent to Affordable Income', 'Median Rent to Affordable Income', 'Affordable Rent to Affordable Income'])

# Display the choropleth graph
choropleth(city, neighborhood, df, color_scale)

st.subheader("Compare monthy rental prices to the average affordable monthly HH income")

st.markdown(
    "Did you know that out of all those who qualify for HUD Affordable Housing (where rent is capped at 30% of household income), only 24% are actually accepted? (Matthews, 2014).  This leaves 76% of those who’s income is 50% of the area median income to fend for themselves in the private rental market place. (HUD: Home Rent Limits)"

    "Explore our interactive dashboard to see how much of one’s monthly paycheck it would take individuals at 50% of the median income to pay for:"
    "- Average HUD Affordable Rent (powered by HUD)"
    "- Average Median Rent (powered by Simplemaps)"
    "- Average Short-Term Rental Monthly Cost (powered by InsideAirbnb)"        

    "Note: Short-Term Rental costs are calculated by daily pricing * 30 days * .564 expected occupancy"

)