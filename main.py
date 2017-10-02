import matplotlib.pyplot as plt
from solcast_frames.latlng import LatLng
from solcast_frames.radiationframehandler import RadiationFrameHandler
from solcast_frames.powerframehandler import PowerFrameHandler

plt.interactive(False) # Turn this off to create plots
location = LatLng(lat=-33.86785, lng=151.215256, name="Sydney", tag="No wild Koalas")
print(location.desc())

# Plot the power `pv_estimate`
# Required fields latlng valid position, capacity as integer > 0
# Adding in an optional keyword argument of an azimuth of 0
# The following optional keyword arguments are recognized by the solcast-py library
# azimuth | range: [-180 to 180] default: 0 in Southern Hemispherer, 180 in Northern Hemisphere
# tilt | range: [0 to 90] | default: 23
# install_date | format: yyyyMMdd Will be ignored if a loss_factor is supplied
# latest | [True, False] | default False
powerEstimatedActuals = PowerFrameHandler.estimated_actuals(location, 5000, azimuth=0)
powerEstimatedActuals.pv_estimate.plot()

# Plot the power `pv_estimate`
# Required fields latlng valid position, capacity as integer > 0
# The following optional keyword arguments are recognized by the solcast-py library
# azimuth | range: [-180 to 180] default: 0 in Southern Hemispherer, 180 in Northern Hemisphere
# tilt | range: [0 to 90] | default: 23
# install_date | format: yyyyMMdd Will be ignored if a loss_factor is supplied
# loss_factor | [0 to 1] | default 0.9
powerForecast = PowerFrameHandler.forecast(location, 5000)
powerForecast.pv_estimate.plot()
plt.show()

# Plot the radiation `ghi` field
# Required fields latlng valid position
# The following optional keyword arguments are recognized by the solcast-py library
# latest | [True, False] | default False
radiationEstimatedActuals = RadiationFrameHandler.estimated_actuals(location)
radiationEstimatedActuals.ghi.plot()
# Plot the radiation `ghi` field
# Required fields latlng valid position
radiationForecast = RadiationFrameHandler.forecast(location)
radiationForecast.ghi.plot()
plt.show()