import solcast as sc
import pandas as pd
from solcast_frames.latlng import LatLng

class RadiationFrameHandler:
    def forecast(lat_lng: LatLng, **kwargs) -> pd.DataFrame:
        """

        :rtype: pd.DataFrame
        """
        data = sc.RadiationForecasts(lat_lng.lat, lat_lng.lng, **kwargs).content["forecasts"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame

    def estimated_actuals(lat_lng: LatLng, **kwargs) -> pd.DataFrame:
        """

        :rtype: pd.DataFrame
        """
        data = sc.RadiationEstimatedActuals(lat_lng.lat, lat_lng.lng, **kwargs).content["estimated_actuals"]
        new_frame = pd.DataFrame(data)
        new_frame.set_index(['period_end'], inplace=True)
        return new_frame