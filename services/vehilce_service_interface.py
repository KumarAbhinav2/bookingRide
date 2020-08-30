import abc

class VehicleServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addVehicle(self, vehileName, vehicleNumber, vehicleType, location):
        pass