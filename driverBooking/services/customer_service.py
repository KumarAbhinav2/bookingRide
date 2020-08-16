from driverBooking.models.customers import Customer
from driverBooking.services.customer_service_interface import CustomerServiceInterface

class CustomerService(CustomerServiceInterface):

    customer_details= {}

    def addCustomer(self, name, phone, lat, lon):
        customer = Customer()
        customer.setName(name)
        customer.setPhone(phone)
        customer.setLatLong(lat, lon)
        CustomerService.customer_details[phone] = customer
        return customer