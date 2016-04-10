#!/usr/bin/python

from twitter import *
# from config import consumer_key, consumer_secret, access_token, access_token_secret
from config import twitter

def search_user_twitter(query):
	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.users.search(q = query)

	for user in results:
		print "@%s (%s): %s" % (user["screen_name"], user["name"], user["location"])


def search_tweets_for_user(screen_name, count):
	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.statuses.user_timeline(screen_name=screen_name, count=count)

	print len(results)
	for tweet in results:
		print '----'
		print tweet


def main():
	# user_name = 'Erin Funk'
	# search_user_twitter(user_name)
	screen_name = 'dys_FUNKtional'
	search_tweets_for_user(screen_name, 50)


if __name__ == '__main__':
	main()
