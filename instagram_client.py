# instagram_client.py
from config import instagram

import requests

class InstagramClient:

    def __init__(self):
        self.api_url = 'https://api.instagram.com/v1/'
        self.user_profile = None
        self.user_media = None


    def find_usernames(self, name):
        """Find an Instagram username given a name."""
        params = {'count': 50, 'q': name, 'access_token': instagram['access_token']}
        response = requests.get(self.api_url + 'users/search?', params=params).json()
        data = response['data']
        usernames = []
        for entry in data:
            usernames.append(entry['username'])

        return usernames


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

        # parse media and grab location names
        items = self.user_media['items']
        location_names = []
        for item in items:
            location = item['location']
            if location:
                location_name = location['name']
                location_names.append(location_name)

        return location_names


    def aggregate_photos(self, username):
        if not self.user_media:
            response = self.get_user_media(username)

        photo_map = {}
        for post in response["items"]:
            photo_map[post["images"]["standard_resolution"]["url"]] = float(post["likes"]["count"]) + float(post["comments"]["count"])
        sort_map = sorted(photo_map, key=photo_map.get, reverse=True)

        return sort_map[:5]
