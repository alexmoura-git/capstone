#Code to join the geojason data with the zipcode information data
# Second part of the code reconciles the neighboorhoods with the ones in the listing file and creates a summary neighbood file

import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
from config import *

def tag_neighborhoods(list_of_cities, include_na=True):
    # Read the zip code file
    uszips_data = pd.read_csv(f'data/city_stats/uszips.csv.gz')

    # Add columns for neighborhood and city
    uszips_data['neighborhood'] = pd.NA
    uszips_data['city_file'] = pd.NA

    for city in list_of_cities:
        # Load GeoJSON
        neighborhoods = gpd.read_file(f'data/{city}/neighbourhoods.geojson')

        # Convert latitude-longitude 
        geometry = [Point(xy) for xy in zip(uszips_data.lng, uszips_data.lat)]
        latlong_gdf = gpd.GeoDataFrame(uszips_data, crs="EPSG:4326", geometry=geometry)

        # Perform the spatial join
        joined_data = gpd.sjoin(latlong_gdf, neighborhoods, how="left", predicate="within")

        # Update neighborhood column
        uszips_data['neighborhood'] = uszips_data['neighborhood'].combine_first(joined_data['neighbourhood'])

        # Update the city_file column 
        matched_indices = joined_data.index[joined_data['neighbourhood'].notna()]
        uszips_data.loc[matched_indices, 'city_file'] = city


    if not include_na:
        uszips_data = uszips_data.dropna(subset=['neighborhood'])

    return uszips_data

# Run function and save to csv in the app folder
df = tag_neighborhoods(list_of_cities, include_na=False)
df.to_csv("app/uszip_augmented_filtered.csv", index=False)




#####-- Create a summarry stats file  -#####

import numpy as np

zip_trimmed=pd.read_csv('app/uszip_augmented_filtered.csv')
zip_trimmed = zip_trimmed [[
     'population', 
     'housing_units', 
     'rent_median', 
     'rent_burden', 
     'neighborhood', 
     'city_file']]
city_neighboorhood=pd.read_csv('app/trimmed_listings.csv')[['neighbourhood_cleansed','city']].drop_duplicates()


# Rename columns to match for merging
zip_trimmed_renamed = zip_trimmed.rename(columns={'city_file': 'city', 'neighborhood': 'neighbourhood_cleansed'})

# Merge
merged_df = zip_trimmed_renamed.merge(city_neighboorhood , on=['city', 'neighbourhood_cleansed'], how='right', indicator=True)


# Define a function for weighted average
def weighted_average(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return np.nan

# Fill NAs in rent_median and rent_burden with the weighted average of the city
merged_df['rent_median'] = merged_df.groupby('city')['rent_median'].transform(lambda x: x.fillna(weighted_average(merged_df, 'rent_median', 'population')))
merged_df['rent_burden'] = merged_df.groupby('city')['rent_burden'].transform(lambda x: x.fillna(weighted_average(merged_df, 'rent_burden', 'population')))

#fill NA in hte population and housing units with a 1
merged_df['population']= merged_df['population'].fillna(1)
merged_df['housing_units']= merged_df['housing_units'].fillna(1)


# Group by city and neighborhood and aggregate
aggregations = {
    'population': 'sum',
    'housing_units': 'sum',
    'rent_median': lambda x: weighted_average(merged_df.loc[x.index], 'rent_median', 'population'),
    'rent_burden': lambda x: weighted_average(merged_df.loc[x.index], 'rent_burden', 'population')
}
cleaned_data = merged_df.groupby(['city', 'neighbourhood_cleansed']).agg(aggregations).reset_index()

cleaned_data.to_csv('app/uszip_stats.csv', index=False) 