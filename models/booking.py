class Booking(object):

    def __init__(self):
        self.booking_id = None
        self.bookings = []

    def setBookingId(self, booking_id):
        self.booking_id = booking_id
        self.bookings.append(self.booking_id)

    # def setDriverId(self, driver_id):
    #     self.driver_id = driver_id
    #
    # def getDriverId(self):
    #     return self.driver_id

    def getBookingId(self):
        return self.booking_id

    def getBookingCount(self):
        return len(self.bookings)





