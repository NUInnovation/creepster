# geolocation_client.py
from config import google

import requests

class GeolocationClient:

    def __init__(self):
        self.api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def find_coordinates(self, location_name):
        """Find coordinates for a location described by location_name."""
        params = {'address': location_name}
        response = requests.get(self.api_url, params=params)
        # naively assumes first result is correct
        result = response.json()['results'][0]
        coordinates = result['geometry']['location']

        return coordinates
