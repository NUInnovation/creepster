#!/usr/bin/python

from app.clients.twitter_client import TwitterClient

def main():
	twitter = TwitterClient()
	following = twitter.get_following('LenaBlietz')
	followers = twitter.get_followers('LenaBlietz')
	print len(following)
	print len(followers)


if __name__ == '__main__':
	main()
