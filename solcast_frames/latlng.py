class LatLng:
    lat = 0
    lng = 0
    tag = None
    name = None

    def __init__(self, *args, **kwargs):
        if 'lat' in kwargs:
            self.lat = kwargs.get('lat')
        if 'lng' in kwargs:
            self.lng = kwargs.get('lng')
        if 'name' in kwargs:
            self.name = kwargs.get('name')
        if 'tag' in kwargs:
            self.tag = kwargs.get('tag')

    def desc(self):
        return "Name: %s Tag:%s [%f, %f]" % (self.name, self.tag, self.lat, self.lng)