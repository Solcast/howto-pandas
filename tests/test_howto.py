import pytest
from solcast_frames.latlng import LatLng
from solcast_frames.radiationframehandler import RadiationFrameHandler
import datetime
from datetime import datetime
from pytz import all_timezones
import pytz
import os

"""
Solcast How to Pandas
"""
def test_howto_pandas_latlng():
    location = LatLng(lat=-33.86785, lng=151.215256, name="Sydney", tag="No wild Koalas",
                      timezone="Australia/Sydney")
    assert location.name == "Sydney"

def get_midnight_now_utc_offset():
    midnight_offset = 0
    for zone_name in all_timezones:
        zone_time = datetime.now(pytz.timezone(zone_name))
        if zone_time.hour == 0:
            midnight_offset = round(zone_time.utcoffset().total_seconds() / 3600)
            break
    return midnight_offset

def test_radiation_request():

    midnight_locations = {
        -12: LatLng(lat=-13.752, lng=-171.7382, name="Apia"),
        -11: LatLng(lat=-13.752, lng=-171.7382, name="Apia"),
        -10: LatLng(lat=21.37124, lng=-157.851, name="Honolulu"),
        -9: LatLng(lat=21.37124, lng=-157.851, name="Honolulu"),
        -8: LatLng(lat=34.0890, lng=-118.2128, name="Los Angeles"),
        -7: LatLng(lat=32.1011, lng=-110.742, name="Phoenix"),
        -6: LatLng(lat=19.3111, lng=-99.31640, name="Mexico City"),
        -5: LatLng(lat=40.9135, lng=-73.6523, name="New York City"),
        -4: LatLng(lat=10.57422, lng=-66.88476, name="Caracas"),
        -3: LatLng(lat=47.51720, lng=-52.77832, name="St. John's"),
        -2: LatLng(lat=-23.56398, lng=-46.5820, name="Sao Paulo"),
        -1: LatLng(lat=-14.55, lng=-23.31, name="Cape Verde"),
        0: LatLng(lat=51.7270, lng=-0.1757, name="London"),
        1: LatLng(lat=7.01366, lng=3.7792, name="Lagos"),
        2: LatLng(lat=30.82678, lng=31.1132, name="Cairo"),
        3: LatLng(lat=55.82597, lng=37.6171, name="Moscow"),
        4: LatLng(lat=35.63944, lng=51.37207, name="Tehran"),
        5: LatLng(lat=24.926294, lng=67.0166, name="Karachi"),
        6: LatLng(lat=28.57482, lng=77.4316, name="Delhi"),
        7: LatLng(lat=22.26876, lng=91.757, name="Dhaka"),
        8: LatLng(lat=-6.140554, lng=106.8310, name="Jakarta"),
        9: LatLng(lat=23.120153, lng=113.2690, name="Tokyo"),
        10: LatLng(lat=35.63944, lng=139.7900, name="Tokyo"),
        11: LatLng(lat=-34.9571, lng=138.6914, name="Adelaide"),
        12: LatLng(lat=-34.01624, lng=151.347, name="Sydney"),
        13: LatLng(lat=-36.7388, lng=174.726, name="Auckland"),
        14: LatLng(lat=-13.752, lng=-171.7382, name="Apia")
    }

    key = os.environ.get('SOLCAST_API_KEY')
    assert key != ""
    where_it_is_dark = midnight_locations[get_midnight_now_utc_offset()]
    location = LatLng(lat=where_it_is_dark.lat, lng=where_it_is_dark.lng, name=where_it_is_dark.name, tag="Near midnight now")
    fx_solcast_radiation = RadiationFrameHandler.forecast(location)

    ghi_now = fx_solcast_radiation['ghi'].iloc[0]
    assert ghi_now == 0
    ghi_next = fx_solcast_radiation['ghi'].iloc[1]
    assert ghi_next == 0
    ghi_and_then = fx_solcast_radiation['ghi'].iloc[2]
    assert ghi_and_then == 0