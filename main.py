from controllers.ride_controller import RideBookingController
from controllers.user_controller import UserController
from services.user_service import UserService
from services.ride_service import RideService
from services.location_service import LocationService
from services.vehicle_service import VehicleService

userController = UserController(UserService())
rideController = RideBookingController(RideService())

location1 = LocationService().addLocation(5, 6)
location2 = LocationService().addLocation(10, 9)
location3 = LocationService().addLocation(11, 4)
location4 = LocationService().addLocation(2, 6)
vehicle1 = VehicleService().addVehicle('prime', 123, 'sedan', location3)
vehicle2 = VehicleService().addVehicle('play', 124, 'sedan', location4)
driver1 = userController.addDriver('d1', 'XXX', '999', vehicle1)
driver2 = userController.addDriver('d2', 'YYY', '456', vehicle2)
customer1 = userController.addCustomer('c1', 'AAA', '342', location1)

rideController.bookRide('r1', 'c1', location1, location2, userController.userService)