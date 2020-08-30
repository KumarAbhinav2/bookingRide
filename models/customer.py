from models.user import User

class Customer(User):

    def __init__(self):
        self.location = None
        self.rides = []

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def setPhone(self, phone):
        self.phone = phone

    def getRides(self):
        return self.rides

    def setRides(self, rides):
        self.rides = rides





