#!/usr/bin/python

from twitter_client import TwitterClient

def main():
	twttr = TwitterClient()
	user_name = 'Miley Cyrus'
	sn = twttr.search_username(user_name)
	twttr.search_tweets_for_user(sn, 50)
	print twttr.aggregate_photos(sn, 50)
	print twttr.user_location(sn)
	print twttr.user_description(sn)
	print twttr.aggregate_hashtags(sn, 1000)
	print twttr.aggregate_retweets(sn, 1000)


if __name__ == '__main__':
	main()
