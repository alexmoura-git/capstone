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

pin_point_df = pd.DataFrame()

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

files = list_files_data_directory('app/data/geojsons','neighbourhoods.geojson')

for file, city in files:
    geo_json = json.load(open(file))
    
    neighborhoods = []
    coordinates = []

    
    for feature in geo_json['features']:
        
        neighborhood = feature['properties']['neighbourhood']
        neighborhoods.append(neighborhood)

       
        geom = shape(feature['geometry'])
        point_within = geom.representative_point()
        lon, lat = point_within.x, point_within.y
        coor = lon, lat
        coordinates.append(coor)
    
    
    city_df = pd.DataFrame({'city': [city]*len(neighborhoods), 'neighborhood': neighborhoods, 'coordinates': coordinates})
    
    
    pin_point_df = pd.concat([pin_point_df, city_df], ignore_index=True)
    
pin_point_df.to_csv('app/choropleth/data/final/pin_point_coordinates.csv')