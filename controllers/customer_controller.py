from math import sqrt
class CustomerController(object):

    def __init__(self, customerService):
        self.customerService = customerService

    def addCustomer(self, id, name, phone, location):
        return self.customerService.addCustomer(id, name, phone, location)


