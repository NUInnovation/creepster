#!/usr/bin/python

from twitter import *
from config import consumer_key, consumer_secret, access_token, access_token_secret

def search_user_twitter(query):
	config = {}

	t = Twitter(
		auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
	)

	results = t.users.search(q = query)
	#
	for user in results:
		print "@%s (%s): %s" % (user["screen_name"], user["name"], user["location"])

def main():
	user_name = 'Melanie Klerer'
	search_user_twitter(user_name)


if __name__ == '__main__':
	main()
