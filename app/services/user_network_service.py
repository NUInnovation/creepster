# user_network_service.py
from app.clients.instagram_client import InstagramClient
from app.clients.twitter_client import TwitterClient
from app.entities.user_network import UserNetwork

class UserNetworkService:

    """
    Service that finds the most likely Instagram username that matches
    a Twitter profile. Takes a Twitter username, finds the user's full name,
    finds all possible Instagram usernames, creates a UserNetwork entity for
    each Instagram username, and finally finds the best match by comparing
    networks.
    """

    def __init__(self, twitter_username):
        self.twitter = TwitterClient()
        self.insta = InstagramClient()
        self.twitter_username = twitter_username
        self.full_name = self.get_fullname(twitter_username)
        self.instagram_usernames = self.get_instagram_usernames(self.full_name)


    def get_fullname(self, twitter_username):
        """Finds a user's full name given a username."""
        user_profile = self.twitter.get_user_profile(twitter_username)
        return user_profile['name']


    def get_instagram_usernames(self, full_name):
        """Finds all possible Instagram usernames."""
        usernames = self.insta.get_usernames(full_name)
        return usernames


    def create_networks(self):
        """Creates all UserNetwork entitites."""
        self.user_networks = []
        for instagram_username in self.instagram_usernames:
            self.user_networks.append(UserNetwork(self.twitter_username, instagram_username))


    def find_match(self):
        """Finds Instagram name of network with highest overlap of following/followers between
        Twitter and Instagram."""
        max_network = max(self.user_networks, key=lambda x:x.average_overlap)
        return max_network.instagram_username


    def get_best_instagram_username(self):
        """Finds best matching Instagram username."""
        self.create_networks()
        best_match = self.find_match()
        return best_match
