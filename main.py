from controllers.customer_controller import CustomerController
from controllers.driver_controller import DriverController
from controllers.ride_booking_controller import RideBookingController
from services.driver_service import DriverService
from services.customer_service import CustomerService
from services.ride_service import RideService
from services.vehicle_service import VehicleService
from services.location_service import LocationService

driverController = DriverController(DriverService())
customerController = CustomerController(CustomerService())
rideController =RideBookingController(RideService())

location1 = LocationService().addLocation(5, 6)
location2 = LocationService().addLocation(10, 9)
location3 = LocationService().addLocation(11, 4)
location4 = LocationService().addLocation(2, 6)
vehicle1= VehicleService().addVehicle('prime', 123, 'sedan', location1)
vehicle2 = VehicleService().addVehicle('play', 124, 'sedan', location2)
driver1 = driverController.addDriver('d1', 'XXX', '999', vehicle1)
driver2 = driverController.addDriver('d2', 'YYY', '456', vehicle2)
customer1 = customerController.addCustomer('c1', 'AAA', '342', location3)




# nearest_driver = bookingController.getNearestDriver(customer1, registered_drivers)
# print(nearest_driver)