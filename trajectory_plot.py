# This code is explained in the readme.md of this repo-

import pandas as pd
import plotly.express as px
import time

latitudes = []
longitudes = []
N = 60 # Sixty for one hour trajectory


# Getting points

for i in range(N):  
    url = "http://api.open-notify.org/iss-now.json" # API URL

    df = pd.read_json(url) # Pandas read JSON data from API
    
    latitudes.append(df["iss_position"]["latitude"])  # We append latitude ISS position to latitudes list
    longitudes.append(df["iss_position"]["longitude"]) # We append longitude ISS position to longitudes list
    
    time.sleep(60) # This is used to separate de point records with one minute


# Plotting
fig = px.line_geo(lat=latitudes, lon=longitudes) # Passing our latitudes and longitudes list as parameter
fig.show()  

# Update to orthographic plot

fig.update_geos(projection_type="orthographic")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()  