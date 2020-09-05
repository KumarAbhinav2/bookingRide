class UserController(object):

    def __init__(self, userService):
        self.userService = userService

    def addDriver(self, id, name, phone, vehicle):
        return self.userService.addDriver(id, name, phone, vehicle)

    def addCustomer(self, id, name, phone, location):
        return self.userService.addCustomer(id, name, phone, location)

    def updateLocation(self, vehicle_number, location):
        return self.userService.updateLocation(vehicle_number, location)