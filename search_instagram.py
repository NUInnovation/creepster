# search_instagram.py
from instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    usernames = insta.find_usernames('Melanie Klerer')
    locations = insta.get_location_names(usernames[0])

    print locations

if __name__ == '__main__':
    main()
