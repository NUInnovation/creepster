# search_411.py

from fouroneone_client import FourOneOneClient

def main():
    four11 = FourOneOneClient()
    print four11.get_addresses('Melanie Klerer')
    print four11.get_lat_longs('Melanie Klerer')

if __name__ == '__main__':
    main()