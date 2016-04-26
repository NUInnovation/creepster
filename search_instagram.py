# search_instagram.py

from app.clients.instagram_client import InstagramClient

def main():
    insta = InstagramClient()
    following = insta.get_following('cata_lena_winemixer')
    followers = insta.get_followers('cata_lena_winemixer')
    print len(following)
    print len(followers)


if __name__ == '__main__':
    main()
