import abc

class DriverServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addDriver(self, id, name, phone, vehicle):
        pass