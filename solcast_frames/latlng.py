class LatLng:
    lat = 0
    lng = 0
    tag = None
    name = None
    timezone = 'Etc/UTC' # Use UTC as default timezone

    def __init__(self, *args, **kwargs):
        if 'lat' in kwargs:
            self.lat = kwargs.get('lat')
        if 'lng' in kwargs:
            self.lng = kwargs.get('lng')
        if 'name' in kwargs:
            self.name = kwargs.get('name')
        if 'tag' in kwargs:
            self.tag = kwargs.get('tag')
        if 'timezone' in kwargs:
            self.timezone = kwargs.get('timezone')
        else:
            self.timezone = 'Etc/UTC'

    def desc(self):
        return "Name: %s Tag:%s [%f, %f] TimeZone: %s" % (self.name, self.tag, self.lat, self.lng, self.timezone)