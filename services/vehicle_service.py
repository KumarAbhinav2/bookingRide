from models.vehicle import Vehicle
from services.vehilce_service_interface import VehicleServiceInterface

class VehicleService(VehicleServiceInterface):

    vehicle_details = {}

    def addVehicle(self, name, number, type, location):
        vehicle = Vehicle()
        vehicle.setVehicleName(name)
        vehicle.setVehicleNumber(number)
        vehicle.setVehicleType(type)
        vehicle.setLocation(location)
        VehicleService.vehicle_details[number] = vehicle
        return vehicle