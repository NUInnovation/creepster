# search_instagram.py
from instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    username = insta.get_username('Jordan Ray')
    media = insta.get_user_media(username)
    print media

if __name__ == '__main__':
    main()
