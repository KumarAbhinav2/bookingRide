from models.location import Location
from services.location_service_interface import LocationServiceInterface

class LocationService(LocationServiceInterface):

    def addLocation(self, lat, lon):
        location = Location()
        location.setLatLon(lat, lon)
        return location
