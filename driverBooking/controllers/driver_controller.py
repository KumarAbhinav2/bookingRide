
class DriverController(object):

    def __init__(self, driverService):
        self.driverService = driverService

    def addDriver(self, name, phone, lat, lon):
        return self.driverService.addDriver(name, phone, lat, lon)

    def getRegisteredDrivers(self):
        return self.driverService.registered_drivers

