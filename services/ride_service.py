from models.ride import Ride
from services.ride_service_interface import RideServiceInterface

class RideService(RideServiceInterface):

    ride_details = {}

    def bookRide(self, rideid, driver, customer, fromLocation, toLocation):
        ride = Ride()
        ride.setDriver(driver)
        ride.setRideId(rideid)
        ride.setCustomer(customer)
        ride.setFromLocation(fromLocation)
        ride.setToLocation(toLocation)
        RideService.ride_details[rideid] = ride
        return ride

