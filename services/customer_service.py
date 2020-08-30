from bookingRide.models.customers import Customer
from services.customer_service_interface import CustomerServiceInterface

class CustomerService(CustomerServiceInterface):

    customer_details= {}

    def addCustomer(self, id, name, phone, location):
        customer = Customer()
        customer.setId(id)
        customer.setName(name)
        customer.setPhone(phone)
        customer.setLocation(location)
        CustomerService.customer_details[id] = customer
        return customer