#!/usr/bin/python

from app.clients.twitter_client import TwitterClient
from run import create_cache_folder, set_environment_vars

def main():
	twitter = TwitterClient()
	followers = twitter.get_verified_followers('LenaBlietz')
	following = twitter.get_verified_following('LenaBlietz')
	print followers
	print following


if __name__ == '__main__':
	create_cache_folder()
	set_environment_vars()
	main()
