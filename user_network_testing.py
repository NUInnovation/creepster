# user_network_testing.py

from app.entities.user_network import UserNetwork
from app.services.user_network_service import UserNetworkService

def main():
    # network_service = UserNetworkService('melanieklerer')
    network = UserNetwork('LenaBlietz', 'cata_lena_winemixer')

    print network.following_overlap
    print network.follower_overlap


if __name__ == '__main__':
    main()
