from models.user import User


class Driver(User):

    def __init__(self):
        self.isAvailable = True
        self.vehicle = None

    def getVehicle(self):
        return self.vehicle

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def isAvailable(self):
        return self.isAvailable

    def setAvailable(self, isavailable):
        self.isAvailable = isavailable










