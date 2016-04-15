# search_instagram.py
from instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    usernames = insta.find_usernames('Melanie Klerer')
    media = insta.get_user_media(usernames[0])
    print media
    print insta.aggregate_photos(usernames[0])

if __name__ == '__main__':
    main()
