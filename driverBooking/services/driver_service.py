from driverBooking.models.driver import Driver
from driverBooking.services.driver_service_interface import DriverServiceInterface


class DriverService(DriverServiceInterface):

    registered_drivers = []

    def addDriver(self, name, phone, lat, lon):
        driver = Driver()
        driver.setName(name)
        driver.setPhone(phone)
        driver.setLatLong(lat, lon)
        DriverService.registered_drivers.append(driver)
        return driver
