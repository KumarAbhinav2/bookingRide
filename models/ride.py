class Ride(object):

    def __init__(self):
        self.rideid = None
        self.driver  = None
        self.customer = None
        self.fromLocation = None
        self.toLocation = None

    def getRideId(self):
        return self.rideid

    def setRideId(self, id):
        self.rideid = id

    def getDriver(self):
        return self.driver

    def setDriver(self, driver):
        self.driver = driver

    def getCustomer(self):
        return self.customer

    def setCustomer(self, customer):
        self.customer = customer

    def getFromLocation(self):
        return self.fromLocation

    def setFromLocation(self, fromlocation):
        self.fromLocation = fromlocation

    def getToLocation(self):
        return self.toLocation

    def setToLocation(self, tolocation):
        self.toLocation = tolocation

