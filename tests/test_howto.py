import pytest
from solcast_frames.latlng import LatLng

"""
Solcast How to Pandas
"""
def test_howto_pandas_latlng():
	location = LatLng(lat=-33.86785, lng=151.215256, name="Sydney", tag="No wild Koalas",
					  timezone="Australia/Sydney")
	assert location.name == "Sydney"