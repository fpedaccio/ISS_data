# ISS DATA WITH PYTHON RESEARCH:earth_americas:

### Plotting ISS trayectory, calculating the velocity over the earth and more.

---

#### Plotting trayectory:
##### _We are going to make a graph of the trajectory of the ISS that is N minutes long. N will be chosen by the user according to their preferences. This means that the program will run and they keep points in a list for N minutes._

##### We will use an API to retrieve ISS current position in latitude and longitude:
http://open-notify.org/Open-Notify-API/ISS-Location-Now/



#### First we need to import the following python modules:
###### _Pandas to read json data from ISS API, plotly to make the plot of the trayectory and time to time.sleep function_
```py
import pandas as pd
import plotly.express as px
import time
```

#### Second we need to initialize the list that will save the latitude and longitude points (every sixty seconds). Also initialize the N variable with time in minutes


```py
latitudes = []
longitudes = []
N = 60 # Sixty for one hour trayectory
```

#### Then we will create the following for loop to keep recording latitude-longitude points separated by one minute
##### _We use for i in range(N), that is the time that the script will keep running (in hours) because we have a time.sleep(60) in the end


```py
for i in range(N):  
    url = "http://api.open-notify.org/iss-now.json" # API URL

    df = pd.read_json(url) # Pandas read JSON data from API
    
    latitudes.append(df["iss_position"]["latitude"])  # We append latitude ISS position to latitudes list
    longitudes.append(df["iss_position"]["longitude"]) # We append longitude ISS position to longitudes list
    
    time.sleep(60) # This is used to separate de point records with one minute
```

#### When the for loop finish the iterating we will have a record of N minutes ISS trayectory. Now we can plot this with Plotly (px.line_geo):
##### _px.line_geo will create a plot with earth map
```py
fig = px.line_geo(lat=latitudes, lon=longitudes) # Passing our latitudes and longitudes list as parameter
fig.show()  
```



