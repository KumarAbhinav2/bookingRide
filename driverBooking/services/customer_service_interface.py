import abc

class CustomerServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addCustomer(self, name, phone, lat, lon):
        pass