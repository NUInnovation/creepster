#!/usr/bin/python

from app.clients.twitter_client import TwitterClient

def main():
	twitter = TwitterClient()
	followers = twitter.get_followers('nevilsgeorge')
	print followers


if __name__ == '__main__':
	main()
