# HowTo Solcast - Python, Pandas, and MatPlotLib

NOTE: You will need to register your user account to obtain an API key [https://solcast.com.au/api/register](https://solcast.com.au/api/register/).  Without an API key you will not be able to successfully obtain valid API results.

### This how to demonstrates working with using the Solcast API to load pandas data frames and then plot different chart data.  Tested and built with Python 3.6.2

This is a demonstration project that shows an example of how to use the [solcast-py](https://github.com/Solcast/solcast-py) library to load a [Pandas](https://github.com/pandas-dev/pandas) data frame and then display a single field graphically using [MatPlotLib](https://github.com/matplotlib/matplotlib).  A familiarity with Python is not required.

### Clone or download this project 

### Install all the require dependencies

If you are not familiar with the python module pip, please refer to this [PIP for Python](https://pip.pypa.io/en/stable/)

```
pip install --upgrade -r requirements.txt
```

### Latitude and Longitude

- First as stated above you will need an API key to make valid API requests to the Solcast system.
- Second for all current library calls you will need a valid Lat/Lng coordinate in the [EPSG:4326](http://spatialreference.org/ref/epsg/wgs-84/) format.  If you are familiar with modern web maps you most likely have used the expected format or a decimal point that expresses a position on the Earth.

Clarification as I often forget the coordinate planes of Latitude and Longitude along with bounds.
![Lat/Lng](/imgs/Lat_Long.gif)

[Credits - Learner.org](http://www.learner.org/jnorth/tm/LongitudeIntro.html)

The Solcast API expects **East** for Longitude and **South** for Latitude to be expressed as a negative numbers

Example Locations on the Globe

Name | Latitude | Longitude
--- | --- | ---
Sydney, Australia | -33.865143 | 151.209900
Mumbai, India |‎ 19.228825 | 72.854118
Tokyo, Japan | 35.6895 | 139.69171
Paris, France | 48.864716 | 2.349014
Los Angeles, USA | 34.052235 | -118.243683

### Power/Radiation library method interaction

In the file **main.py** is a minimal set of commands to obtain the following charts.  The break in the continuity between the Estimated Actuals and the Forecast predicted values on the time scale is due to that the time period falls between an in place Estimated Actual result being recorded and a next period available Forecast.  Currently all period results are broken into **30** minute timestamp periods.  This howto uses the `period_end` fields as the indexed field for the DataFrames (x - axis on the following charts)

**Power** Estimated Actuals with Forecast (`pv_estimate` over `period_end`)
![Power Graph](/imgs/power.png)

**Radiation** Estimated Actuals with Forecast (`ghi` over `period_end`)
![Radiation Graph](/imgs/radiation.png)

### Details of Solcast Python Client Library [Solcast Python API client library ](https://github.com/Solcast/solcast-py)

The Solcast Python library is designed as a synchronous web service and does not include the graphing or advanced data options of Pandas/MatPlotLib.

The PowerFrameHandler.py and RadiationFrameHandler.py classes in this howto under solcast_frames example convert the list value resultsets into pandas dataframes aligned and indexed by the period_end DateTime field (all datetimes are expressed in UTC timezone).

Example data results for [Power](https://solcast.com.au/api/docs/pv_power.html) DataFrames with columns available:
### Estimated Actuals and Forecast

```
                            period  pv_estimate
period_end                                     
2017-10-02 19:30:00+00:00 00:30:00     0.000000
2017-10-02 20:00:00+00:00 00:30:00    27.628064
2017-10-02 20:30:00+00:00 00:30:00   243.625359
```

Example data results for [Radiation](https://solcast.com.au/api/docs/radiation.html) DataFrames with columns available:

### Estimated Actuals

```
                           cloud_opacity  dhi  dni  ebh  ghi   period
period_end                                                           
2017-10-02 13:00:00+00:00             26    0    0    0    0 00:30:00
2017-10-02 12:30:00+00:00             31    0    0    0    0 00:30:00
2017-10-02 12:00:00+00:00              0    0    0    0    0 00:30:00
```

### Forecast

```
                           air_temp  azimuth  cloud_opacity  dhi  dni  dni10  dni90  ebh  ghi  ghi10  ghi90   period  zenith  
period_end                                                                                                                    
2017-10-02 19:30:00+00:00        17      -97             17    1    0      0      0    0    1      1      1 00:30:00      94  
2017-10-02 20:00:00+00:00        17      -93             33   13   10      4     27    2   15     12     19 00:30:00      88  
2017-10-02 20:30:00+00:00        17      -88              7   45  196     43    275   33   79     57     86 00:30:00      82 
```