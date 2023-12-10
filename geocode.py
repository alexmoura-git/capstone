#Code to join the geojason data with the zipcode information data

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