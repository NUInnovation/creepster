# search_instagram.py
from instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    usernames = insta.find_usernames('Miley Cyrus')
    media = insta.get_user_media(usernames[0])

    print media

if __name__ == '__main__':
    main()
