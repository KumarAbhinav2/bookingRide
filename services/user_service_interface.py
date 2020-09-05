import abc

class UserServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addCustomer(self, id, name, phone, location):
        pass

    @abc.abstractmethod
    def addDriver(self, id, name, phone, vehicle):
        pass

    @abc.abstractmethod
    def updateLocation(self, vehicle_number, location):
        pass