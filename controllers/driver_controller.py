
class DriverController(object):

    def __init__(self, driverService):
        self.driverService = driverService

    def addDriver(self, id, name, phone, vehicle):
        return self.driverService.addDriver(id, name, phone, vehicle)

