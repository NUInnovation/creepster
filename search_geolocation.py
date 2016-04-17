# search_geolocation.py
from geolocation_client import GeolocationClient

def main():
    client = GeolocationClient()
    response = client.find_coordinates('Empire State Building')

    print response

if __name__ == '__main__':
    main()
