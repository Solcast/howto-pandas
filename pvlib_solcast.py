import pandas as pd
import matplotlib.pyplot as plt
import datetime
from solcast_frames.latlng import LatLng
from solcast_frames.radiationframehandler import RadiationFrameHandler
from solcast_frames.powerframehandler import PowerFrameHandler

plt.interactive(False)
location = LatLng(lat=32.2, lng=-110.9, name="Tucson", tag="Cactus Land")
print(location.desc())

#
#
#
# Following code is from http://pvlib-python.readthedocs.io/en/latest/forecasts.html#pv-power-forecast
# PV Power Forecast
#
#
# import pvlib forecast models
from pvlib.forecast import GFS, NAM, NDFD, HRRR, RAP

# specify location timezone for pvlib (Tucson, AZ)
tz = 'US/Arizona'

# specify time range.
start = pd.Timestamp(datetime.date.today(), tz=tz)
end = start + pd.Timedelta(days=7)

from pvlib.pvsystem import PVSystem, retrieve_sam
from pvlib.tracking import SingleAxisTracker
from pvlib.modelchain import ModelChain

sandia_modules = retrieve_sam('sandiamod')
cec_inverters = retrieve_sam('cecinverter')
module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
inverter = cec_inverters['SMA_America__SC630CP_US_315V__CEC_2012_']

# model a big tracker for more fun
system = SingleAxisTracker(module_parameters=module,
                           inverter_parameters=inverter,
                           modules_per_string=15,
                           strings_per_inverter=300)

# fx is a common abbreviation for forecast
fx_model = GFS()
fx_data = fx_model.get_processed_data(location.lat, location.lng, start, end)


radiationForecast = RadiationFrameHandler.forecast(location)
plt.plot(fx_data.ghi, label="ghi - PVLIB (GFS)")
plt.plot(radiationForecast.ghi, label="ghi - Solcast", linestyle='dashdot')

plt.plot(fx_data.dhi, label="dhi - PVLIB (GFS)")
plt.plot(radiationForecast.dhi, label="dhi - Solcast", linestyle='dashdot')

plt.plot(fx_data.dni, label="dni - PVLIB (GFS)")
plt.plot(radiationForecast.dni, label="dni - Solcast", linestyle='dashdot')

plt.legend()
plt.show()

# use a ModelChain object to calculate modeling intermediates
mc = ModelChain(system, fx_model.location)
# extract relevant data for model chain
mc.run_model(fx_data.index, weather=fx_data)

# Using this number for capacity comes from
# https://github.com/pvlib/pvlib-python/blob/f67ecfff730a5360fe7e57a8aa31c9d09aea292c/pvlib/data/sam-library-cec-inverters-2015-6-30.csv
# CEC Inverter - SMA America: SC630CP-US 315V [CEC 2012]
# With Terminiology from http://energy.sandia.gov/wp-content/gallery/uploads/Performance-Model-for-Grid-Connected-Photovoltaic-Inverters.pdf Page 15
powerForecast = PowerFrameHandler.forecast(location, 653000)

plt.plot(mc.ac, label="PVLIB");
plt.plot(powerForecast.pv_estimate, label="Solcast", linestyle='dashdot');
plt.ylabel('AC Power (W)');
plt.legend()
plt.show()

