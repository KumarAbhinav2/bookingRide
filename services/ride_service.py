from models.ride import Ride
from services.ride_service_interface import RideServiceInterface
from utils import getEuclideanDistance
from configs import MAX_DISTANCE
from exceptions import DriversNotAvailableException


class RideService(RideServiceInterface):

    ride_details = {}

    def bookRide(self, rideid, riderid, fromLocation, toLocation, user):
        rider = user.customer_details[riderid]
        driver = self.fetch_nearest_driver(user, fromLocation)
        if not driver:
            raise DriversNotAvailableException
        ride = Ride()
        ride.setRideId(rideid)
        ride.setDriver(driver)
        ride.setCustomer(rider)
        ride.setFromLocation(fromLocation)
        ride.setToLocation(toLocation)
        RideService.ride_details[rideid] = ride
        rider.getRides().append(ride)
        return ride

    def fetch_nearest_driver(self, user, location):
        available_drivers = []
        for driver in user.driver_details.values():
            if driver.isAvailable():
                toLocation = driver.getVehicle().getLocation()
                res = getEuclideanDistance(location, toLocation)
                if res < MAX_DISTANCE:
                    available_drivers.append(driver)
        available_drivers.sort()
        return available_drivers[0]


