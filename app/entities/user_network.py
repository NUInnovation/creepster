# user_network.py
from app.clients.instagram_client import InstagramClient
from app.clients.twitter_client import TwitterClient

class UserNetwork:

    """Represents the social network of a given individual."""

    def __init__(self, twitter_username, insta_username):
        self.twitter_username = twitter_username
        self.instagram_username = insta_username

        # let's go!
        self.create_network()
        self.calculate_following_overlap()
        self.calculate_follower_overlap()
        self.calculate_average_overlap()


    def create_network(self):
        """Creates a simple model of a social network using Twitter and Instagram."""
        # get Twitter network
        twitter = TwitterClient()
        self.twitter_following = twitter.get_following(self.twitter_username)
        self.twitter_followers = twitter.get_followers(self.twitter_username)

        # get Instagram network
        insta = InstagramClient()
        self.instagram_following = insta.get_following(self.instagram_username)
        self.instagram_followers = insta.get_followers(self.instagram_username)


    def calculate_following_overlap(self):
        """Calculate overlap percentages between Twitter and Instagram following."""
        count = 0
        for t_following in self.twitter_following:
            for i_following in self.instagram_following:
                # string comparison
                if t_following['name'].lower() == i_following['full_name'].lower():
                    count += 1

        self.following_overlap = float(count/len(self.twitter_following)) % 100


    def calculate_follower_overlap(self):
        """Calculate overlap percentages between Twitter and Instagram followers."""
        count = 0
        for t_follower in self.twitter_followers:
            for i_follower in self.instagram_followers:
                # string comparison
                if t_follower['name'].lower() == i_follower['full_name'].lower():
                    count += 1

        self.follower_overlap = float(count/len(self.twitter_followers)) % 100


    def calculate_average_overlap(self):
        """Calculates average between following and follower overlaps."""
        self.average_overlap = (self.following_overlap + self.follower_overlap) / float(2)
