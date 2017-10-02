import solcast as sc
import pandas as pd

class RadiationFrameHandler:
    def forecast(lat_lng, **kwargs):
        """

        :rtype: object
        """
        data = sc.RadiationForecasts(lat_lng.lat, lat_lng.lng, **kwargs).content["forecasts"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame

    def estimated_actuals(lat_lng, **kwargs):
        """

        :rtype: object
        """
        data = sc.RadiationEstimatedActuals(lat_lng.lat, lat_lng.lng, **kwargs).content["estimated_actuals"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame