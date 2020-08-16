import abc


class BookingServiceInteface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addBooking(self):
        pass
