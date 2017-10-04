import pandas as pd
import solcast as sc
from solcast_frames.latlng import LatLng

class PowerFrameHandler:
    def forecast(lat_lng: LatLng, capacity: int, **kwargs) -> pd.DataFrame:
        """

        :rtype: pd.DataFrame
        """
        data = sc.PvPowerForecasts(lat_lng.lat, lat_lng.lng, capacity, **kwargs).content["forecasts"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame

    def estimated_actuals(lat_Lng: LatLng, capacity: int, **kwargs) -> pd.DataFrame:
        """

        :rtype: pd.DataFrame
        """
        data = sc.PvPowerEstimatedActuals(lat_Lng.lat, lat_Lng.lng, capacity, **kwargs).content["estimated_actuals"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame