# ISS DATA WITH PYTHON RESEARCH

### Plotting ISS trayectory, calculating the velocity over the earth and more.

---

#### Plotting trayectory:

##### We will use an API to retrieve ISS current position in latitude and longitude:
http://open-notify.org/Open-Notify-API/ISS-Location-Now/



#### First we need to import the following python modules:
###### _Pandas to read json data from ISS API, plotly to make the plot of the trayectory and time to time.sleep fumction_
```py
import pandas as pd
import plotly.express as px
import time
```




