import abc

class RideServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def bookRide(self, rideid, driver, customer, fromLocation, toLocation):
        pass
