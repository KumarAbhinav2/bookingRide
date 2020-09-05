from services.user_service_interface import UserServiceInterface
from models.customer import Customer
from models.driver import Driver
from exceptions import VehicleNotFoundException


class UserService(UserServiceInterface):

    customer_details= {}
    driver_details = {}
    vehicle_details = {}

    def addCustomer(self, id, name, phone, location):
        customer = Customer()
        customer.setId(id)
        customer.setName(name)
        customer.setPhone(phone)
        customer.setLocation(location)
        UserService.customer_details[id] = customer
        return customer

    def addDriver(self, id, name, phone, vehicle):
        driver = Driver()
        driver.setId(id)
        driver.setName(name)
        driver.setPhone(phone)
        driver.setVehicle(vehicle)
        UserService.driver_details[id] = driver
        return driver

    def updateLocation(self, vehicle_number, location):
        if vehicle_number in UserService.vehicle_details:
            UserService.vehicle_details[vehicle_number].setLocation = location
        else:
            raise VehicleNotFoundException


