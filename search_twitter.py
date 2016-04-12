#!/usr/bin/python

from twitter import *
# from config import consumer_key, consumer_secret, access_token, access_token_secret
from config import twitter

def search_username(query):
	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.users.search(q = query)
	user = results[0]
	return user["screen_name"]


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

	for tweet in results:
		print '----'
		print tweet["text"]

def is_geo_enabled(screen_name):
	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)
	results = t.users.search(q=screen_name, count=1)
	return results[0]["geo_enabled"]

def user_location(screen_name):
	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.users.search(q=screen_name, count=1)
	return results[0]["location"]

def user_description(screen_name):
	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.users.search(q=screen_name, count=1)
	return results[0]["description"]

def search_geo_for_user(screen_name, count):
	if is_geo_enabled(screen_name) == False:
		print "Not Geo-Enabled"
		return

	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)


	results = t.statuses.user_timeline(screen_name=screen_name, count=count)

	for tweet in results:
		if tweet["place"] != None:
			print tweet["place"]

def aggregate_hashtags(screen_name, count):

	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.statuses.user_timeline(screen_name=screen_name, count=count)
	hashtag_map = {}
	for tweet in results:
		for hashtag in tweet["entities"]["hashtags"]:
			name = hashtag["text"]
			if not name in hashtag_map:
				hashtag_map[name] = 1
			else:
				hashtag_map[name] = hashtag_map[name] + 1

	sort_hash = sorted(hashtag_map, key=hashtag_map.get, reverse=True)
	return sort_hash[:4]

def aggregate_retweets(screen_name, count):

	t = Twitter(
		auth = OAuth(
			twitter['access_token'],
			twitter['access_token_secret'],
			twitter['consumer_key'],
			twitter['consumer_secret']
		)
	)

	results = t.statuses.user_timeline(screen_name=screen_name, count=count)
	retweet_map = {}
	for tweet in results:
		if tweet["text"].startswith('RT', 0, 2):
			handle = tweet["retweeted_status"]["user"]["name"]
			if not handle in retweet_map:
				retweet_map[handle] = 1
			else:
				retweet_map[handle] = retweet_map[handle] + 1


	sort_tweet = sorted(retweet_map, key=retweet_map.get, reverse=True)
	return sort_tweet[:4]


def main():
	user_name = 'Miley Cyrus'
	sn = search_username(user_name)
	search_tweets_for_user(sn, 50)
	print user_location(sn)
	print user_description(sn)
	print aggregate_hashtags(sn, 1000)
	print aggregate_retweets(sn, 1000)


if __name__ == '__main__':
	main()
