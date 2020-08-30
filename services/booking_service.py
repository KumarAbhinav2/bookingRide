from services.booking_service_interface import BookingServiceInteface
from models import Booking


class BookingService(BookingServiceInteface):
    booking_details = {}

    def addBooking(self, cust, driver):
        booking = Booking()
        booking.setBookingId(driver.phone)
        BookingService.booking_details[driver] = cust
        return False

    def getBookings(self):
        return len(BookingService.booking_details)





