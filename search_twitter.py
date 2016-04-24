#!/usr/bin/python

from app.clients.twitter_client import TwitterClient

def main():
	twitter = TwitterClient()
	profile = twitter.get_user_profile('nevilsgeorge')
	print profile


if __name__ == '__main__':
	main()
