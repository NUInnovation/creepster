# search_geolocation.py
from geolocation_client import GeolocationClient

def main():
    client = GeolocationClient()
    response = client.find_coordinates('Northwestern University')

    print response

if __name__ == '__main__':
    main()
