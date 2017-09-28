import pandas as pd
import solcast as sc

class PowerFrameHandler:

    def forecast(lat_lng, capacity, **kwargs):
        """

        :rtype: object
        """
        data = sc.PvPowerForecasts(lat_lng.lat, lat_lng.lng, capacity, **kwargs).content["forecasts"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame

    def estimated_actuals(lat_Lng, capacity, **kwargs):
        """

        :rtype: object
        """
        data = sc.PvPowerEstimatedActuals(lat_Lng.lat, lat_Lng.lng, capacity, **kwargs).content["estimated_actuals"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame