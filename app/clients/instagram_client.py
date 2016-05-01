# instagram_client.py
from config import instagram
from app.exceptions.media_missing_exception import MediaMissingException
from app.exceptions.no_locations_exception import NoLocationsException

import requests

class InstagramClient:

    def __init__(self):
        self.api_url = 'https://api.instagram.com/v1/'
        self.user_profile = None
        self.user_media = None


    def get_username(self, name):
        """Find an Instagram username given a name."""
        params = {'count': 50, 'q': name, 'access_token': instagram['access_token']}
        response = requests.get(self.api_url + 'users/search?', params=params).json()
        data = response['data']
        usernames = [entry['username'] for entry in data]
        if len(usernames) == 0:
            raise MediaMissingException('No Account Found!')
        return usernames[0]

    def get_usernames(self, name):
        """Find all Instagram usernames given a name."""
        params = {'count': 50, 'q': name, 'access_token': instagram['access_token']}
        response = requests.get(self.api_url + 'users/search?', params=params).json()
        data = response['data']
        usernames = [entry['username'] for entry in data]
        if len(usernames) == 0:
             raise MediaMissingException('No Account Found!')
        return usernames


    def get_user(self, username):
        """Get user profile given a username."""
        params = {'q': username, 'access_token': instagram['access_token']}
        response = requests.get(self.api_url + 'users/search?', params=params).json()
        data = response['data']
        return data[0]


    def get_user_profile(self, user_id):
        """Get more information about a user given a user_id."""
        if not self.user_profile:
            url = self.api_url + 'users/' + user_id + '/?'
            params = {'access_token': instagram['access_token']}
            response = requests.get(url + 'users/' + user_id, params=params)
            self.user_profile = response.json()

        return self.user_profile


    def get_user_media(self, username):
        """Get all media given a username."""
        if not self.user_media:
            url = 'https://instagram.com/' + username + '/media'
            response = requests.get(url)
            self.user_media = response.json()

        return self.user_media


    def get_location_names(self, username):
        """Get all locations from Instagram posts of the given username."""
        if not self.user_media:
            self.get_user_media(username)

        # raise relevant exception if no media retrieved
        if len(self.user_media['items']) == 0:
            raise MediaMissingException('No user media returned from API!')

        # parse media and grab location names
        items = self.user_media['items']
        location_names = []
        for item in items:
            location = item['location']
            if location:
                location_name = location['name']
                location_names.append(location_name)

        # raise relevant exception if no locations provided
        if len(location_names) == 0:
            raise NoLocationsException('No locations provided in user\'s posts!')

        return location_names


    def aggregate_photos(self, username):
        """Aggregate all photos of a given user."""
        if not self.user_media:
            self.get_user_media(username)

        if len(self.user_media['items']) == 0:
            raise MediaMissingException('No user media returned from API!')

        photo_map = {}
        for post in self.user_media["items"]:
            photo_map[post["images"]["standard_resolution"]["url"]] = float(post["likes"]["count"]) + float(post["comments"]["count"])
        sort_map = sorted(photo_map, key=photo_map.get, reverse=True)

        return sort_map[:5]


    def get_following(self, username):
        """Returns user profiles for 100 friends of a given user."""
        user = self.get_user(username)
        user_id = user['id']
        params = {'access_token': instagram['access_token'], 'count': 100}
        url = self.api_url + 'users/' + user_id + '/follows?'
        response = requests.get(url, params=params).json()
        if response['meta']['code'] != 200:
            raise MediaMissingException('Unable to access account!')
        return response['data']


    def get_followers(self, username):
        """Returns user profiles for 100 followers of a given user."""
        user = self.get_user(username)
        user_id = user['id']
        params = {'access_token': instagram['access_token'], 'count': 100}
        url = self.api_url + 'users/' + user_id + '/followed-by?'
        response = requests.get(url, params=params).json()
        if response['meta']['code'] != 200:
            raise MediaMissingException('Unable to access account!')
        return response['data']
