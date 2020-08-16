import abc

class DriverServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addDriver(self, name, phone, lat, lon):
        pass