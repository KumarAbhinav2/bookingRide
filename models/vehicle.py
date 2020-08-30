class Vehicle(object):

    def __init__(self):
        self.vehicleName = None
        self.vehicleNumber = None
        self.vehicleType = None
        self.location = None

    def getVehicleName(self):
        return self.vehicleName

    def setVehicleName(self, name):
        self.vehicleName = name

    def getVehicleNumber(self):
        return self.vehicleNumber

    def setVehicleNumber(self, number):
        self.vehicleNumber = number

    def getVehicleType(self):
        return self.vehicleType

    def setVehicleType(self, name):
        self.vehicleType = name

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location