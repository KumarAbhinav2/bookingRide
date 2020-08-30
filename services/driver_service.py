from models.driver import Driver
from services.driver_service_interface import DriverServiceInterface


class DriverService(DriverServiceInterface):

    driver_details = {}

    def addDriver(self, id, name, phone, vehicle):
        driver = Driver()
        driver.setId(id)
        driver.setName(name)
        driver.setPhone(phone)
        driver.setVehicle(vehicle)
        DriverService.driver_details[id] = driver
        return driver
