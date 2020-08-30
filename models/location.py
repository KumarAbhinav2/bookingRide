class Location(object):

    def __init__(self):
        self.lat = None
        self.lon = None

    def setLatLon(self, lat, lon):
        self.lat, self.lon = lat, lon

    def getLatLon(self):
        return self.lat, self.lon
