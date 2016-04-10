# search_instagram.py

import requests
from config import instagram
from instagram.client import InstagramAPI

api_url = 'https://api.instagram.com/v1/'

def find_user(name):
    """Find an Instagram user given a name."""
    params = {'count': 50, 'q': name, 'access_token': instagram['access_token']}
    response = requests.get(api_url + 'users/search?', params=params)

    return response.json()

def get_user(username):
    """Get more information about a user given a username."""
    url = api_url + 'users/' + username + '/?'
    params = {'access_token': instagram['access_token']}
    response = requests.get(url + 'users/' + username, params=params)

    return response.json()

def main():
    print find_user('Nevil George')
    # print get_user('647926477')


if __name__ == '__main__':
    main()
