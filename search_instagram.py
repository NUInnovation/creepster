# search_instagram.py
from instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    usernames = insta.get_username('Melanie Klerer')
    media = insta.get_user_media(usernames)
    print media
    print insta.aggregate_photos(usernames)

if __name__ == '__main__':
    main()
