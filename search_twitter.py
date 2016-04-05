#!/usr/bin/python


from twitter import *

def search_user_twitter(query):
	config = {}
	execfile("config.py", config)

	twitter = Twitter(
			auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

	results = twitter.users.search(q = query)

	for user in results:
		print "@%s (%s): %s" % (user["screen_name"], user["name"], user["location"])
