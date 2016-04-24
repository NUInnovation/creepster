# search_instagram.py

from app.clients.instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    following = insta.get_following('melanieklerer')
    print following


if __name__ == '__main__':
    main()
