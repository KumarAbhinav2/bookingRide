from math import sqrt

class RideBookingController(object):

    def __init__(self, rideService):
        self.rideService = rideService

    def bookRide(self, rideid, driver, customer, fromLocation, toLocation):
        self.rideService.bookRide(rideid, driver, customer, fromLocation, toLocation)

    def addBooking(self, cust, driver):
        res = self.bookingService.addBooking(cust, driver)
        if not res:
            return "False"
        return True

    def getNearestDriver(self, customer, registered_drivers):
        import pdb;pdb.set_trace()
        available_drivers = set(registered_drivers) - set(self.bookingService.booking_details)
        cust_lat_long = customer.getLatLong()
        min = float('inf')
        nearest_driver = None
        for driver in available_drivers:
            driver_lat_log = driver.getLatLong()
            dist = self.getEuclideanDistance(cust_lat_long, driver_lat_log)
            if dist < min:
                min = dist
                nearest_driver = driver
        return nearest_driver



