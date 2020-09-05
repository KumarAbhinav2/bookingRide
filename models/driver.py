from models.user import User


class Driver(User):

    def __init__(self):
        self.isavailable = True
        self.vehicle = None

    def getVehicle(self):
        return self.vehicle

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def isAvailable(self):
        return self.isavailable

    def setAvailable(self, isavailable):
        self.isAvailable = isavailable










