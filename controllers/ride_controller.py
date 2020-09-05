class RideBookingController(object):

    def __init__(self, rideService):
        self.rideService = rideService

    def bookRide(self, rideid, riderid, fromLocation, toLocation, user):
        self.rideService.bookRide(rideid, riderid, fromLocation, toLocation, user)



