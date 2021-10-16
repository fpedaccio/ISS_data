
# This code is explained in the readme.md of this repo-

import pandas as pd # Pandas to read API data
import time # Time for time.sleep
import geopy.distance # Geopy to get distance between two lat-lon points
import requests # Get another API data
import json # Read that data


# We need to initialize two empty list to save latitudes and longitudes

lat = []
long = []


for i in range(2):  # for in range(2) because we want two lat-lon points

    url = "http://api.open-notify.org/iss-now.json" # API url

    df = pd.read_json(url) # Read API Json data with Pandas

    lat.append(df["iss_position"]["latitude"]) # Append latitude to lat list
    long.append(df["iss_position"]["longitude"]) # Append longitude to long list

    time.sleep(60) # Wait 60 seconds to record the second lat-lon point

coords_1 = (lat[0], long[0]) 
coords_2 = (lat[1], long[1])

distance = (
geopy.distance.distance(coords_1, coords_2).m
) # Distance between the points in meters


iss_alt_url = "https://api.wheretheiss.at/v1/satellites/25544"
r = requests.get(iss_alt_url)
r = r.text
r = json.loads(r)

iss_alt = int(r["altitude"]) # IN KM

earth_radius = 6371 # in KM
distance_corrected = (distance * (earth_radius+iss_alt)/earth_radius)


speed = distance_corrected/60 


print(round(speed*3.6, 3), "KM/H") # Multiplied by 3.6 to convert from m/s to km/h. Rounded by 3.


