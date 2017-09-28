import matplotlib.pyplot as plt
from solcast_frames.latlng import LatLng
from solcast_frames.radiationframehandler import RadiationFrameHandler
from solcast_frames.powerframehandler import PowerFrameHandler

plt.interactive(False)
location = LatLng(lat=-33.86785, lng=151.215256, name="Sydney", tag="No wild Koalas")
print(location.desc())

# Plot the power `pv_estimate`
powerEstimatedActuals = PowerFrameHandler.estimated_actuals(location, 5000, azimuth=0)
powerEstimatedActuals.pv_estimate.plot()
powerForecast = PowerFrameHandler.forecast(location, 5000)
powerForecast.pv_estimate.plot()
plt.show()

# Plot the radiation `ghi` field
radiationEstimatedActuals = RadiationFrameHandler.estimated_actuals(location)
radiationEstimatedActuals.ghi.plot()
radiationForecast = RadiationFrameHandler.forecast(location)
radiationForecast.ghi.plot()
plt.show()