# instagram_client.py
from config import instagram

class InstagramClient:

    def __init__(self):
        self.api_url = 'https://api.instagram.com/v1/'


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
        url = self.api_url + 'users/' + user_id + '/?'
        params = {'access_token': instagram['access_token']}
        response = requests.get(url + 'users/' + user_id, params=params)

        return response.json()


    def get_user_media(self, username):
        """Get all media given a username."""
        url = 'https://instagram.com/' + username + '/media'
        response = requests.get(url)

        return response.json()
