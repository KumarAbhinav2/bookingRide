import abc

class CustomerServiceInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addCustomer(self, id, name, phone, location):
        pass