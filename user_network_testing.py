# user_network_testing.py

from app.entities.user_network import UserNetwork
from app.services.user_network_service import UserNetworkService

def main():
    # network_service = UserNetworkService('melanieklerer')
    network = UserNetwork('nevilsgeorge', 'neviiil')
    network.calculate_following_overlap()
    network.calculate_follower_overlap()


if __name__ == '__main__':
    main()
