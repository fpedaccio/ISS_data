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
lati = []
long = []
N = 60 # Sixty for one hour trayectory
```





