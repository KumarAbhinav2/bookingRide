from math import sqrt
class CustomerController(object):

    def __init__(self, customerService):
        self.customerService = customerService

    def addCustomer(self, name, phone, lat, lon):
        return self.customerService.addCustomer(name, phone, lat, lon)


