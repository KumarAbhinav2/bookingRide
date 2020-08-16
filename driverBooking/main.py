from driverBooking.controllers.customer_controller import CustomerController
from driverBooking.controllers.driver_controller import DriverController
from driverBooking.controllers.booking_controller import BookingController
from driverBooking.services.driver_service import DriverService
from driverBooking.services.customer_service import CustomerService
from driverBooking.services.booking_service import BookingService

driverController = DriverController(DriverService())
customerController = CustomerController(CustomerService())
bookingController = BookingController(BookingService())

driver1 = driverController.addDriver('X', '9', 5, 5)
driver2 = driverController.addDriver('Y', '8', 7, 4)
driver3 = driverController.addDriver('Z', '7', 6, 7)
customer1 = customerController.addCustomer('Abhi', '99', 5, 2)

registered_drivers = driverController.getRegisteredDrivers()
nearest_driver = bookingController.getNearestDriver(customer1, registered_drivers)
print(nearest_driver)