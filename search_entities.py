# search_entiites.py

from entity_recongnition_client import EntityRecongnitionClient
from twitter_client import TwitterClient 
from instagram_client import InstagramClient 

def main():
    erc = EntityRecongnitionClient()
    user_name = 'Lena Blietz'
    tc = TwitterClient()
    ic = InstagramClient()
    sn_twitter = tc.search_username(user_name)
    sn_instagram = ic.get_username(user_name)
    print "-----------Instagram Entities --------------"
    print erc.get_entities_from_instagram(sn_instagram)
    print "-----------Twitter Entities --------------"
    print erc.get_entities_from_tweets(sn_twitter,50)

if __name__ == '__main__':
    main()