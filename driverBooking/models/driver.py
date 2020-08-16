class Driver(object):

    def __init__(self):
        self.name = None
        self.phone = None
        self.lat = None
        self.long = None
        self.booked = False

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

    def setLatLong(self, lat, long):
        self.lat = lat
        self.long = long

    def getLatLong(self):
        return self.lat, self.long

    def setBooked(self):
        self.booked = True

    def getBooked(self):
        return self.booked

    def __str__(self):
        return self.name





