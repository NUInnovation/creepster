# twitter_client.py

#!/usr/bin/python

from twitter import *
from config import twitter
from app.exceptions.no_twitter_account_exception import NoTwitterAccountException

class TwitterClient:
	def __init__(self):
		self.t = Twitter(auth = OAuth(twitter['access_token'], twitter['access_token_secret'], twitter['consumer_key'], twitter['consumer_secret']))
		self.timeline = None


	def search_username(self, query):
		results = self.t.users.search(q = query)
		if len(results) == 0:
			raise NoTwitterAccountException('No twitter account found!')
		user = results[0]
		return user["screen_name"]


	def search_usernames(self, query):
		"""Return all usernames with the given query."""
		results = self.t.users.search(q=query)
		usernames = [(user['name'], user['screen_name']) for user in results]
		return usernames


	def search_tweets_for_user(self, screen_name, count):
		if not self.timeline:
			try:
				self.timeline = self.t.statuses.user_timeline(screen_name=screen_name, count=count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		text = []
		for tweet in self.timeline:
			#print '----'
			#print tweet["text"]
			text.append(tweet["text"])
		return text


	def is_geo_enabled(self, screen_name):
		results = self.t.users.search(q=screen_name, count=1)
		return results[0]["geo_enabled"]


	def user_location(self, screen_name):
		results = self.t.users.search(q=screen_name, count=1)
		return results[0]["location"]


	def user_description(self, screen_name):
		results = self.t.users.search(q=screen_name, count=1)
		return results[0]["description"]


	def search_geo_for_user(self, screen_name, count):
		if is_geo_enabled(screen_name) == False:
			print "Not Geo-Enabled"
			return

		if not self.timeline:
			try:
				self.timeline = self.t.statuses.user_timeline(screen_name=screen_name, count=count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		for tweet in self.timeline:
			if tweet["place"] != None:
				print tweet["place"]


	def aggregate_hashtags(self, screen_name, count):
		if not self.timeline:
			try:
				self.timeline = self.t.statuses.user_timeline(screen_name=screen_name, count=count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		hashtag_map = {}
		for tweet in self.timeline:
			for hashtag in tweet["entities"]["hashtags"]:
				name = hashtag["text"]
				if not name in hashtag_map:
					hashtag_map[name] = 1
				else:
					hashtag_map[name] = hashtag_map[name] + 1

		sort_hash = sorted(hashtag_map, key=hashtag_map.get, reverse=True)
		return sort_hash[:4]


	def aggregate_retweets(self, screen_name, count):
		if not self.timeline:
			try:
				self.timeline = self.t.statuses.user_timeline(screen_name=screen_name, count=count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		retweet_map = {}
		for tweet in self.timeline:
			if tweet["text"].startswith('RT', 0, 2):
				try:
					handle = tweet["retweeted_status"]["user"]["name"]
					if not handle in retweet_map:
						retweet_map[handle] = 1
					else:
						retweet_map[handle] = retweet_map[handle] + 1
				except Exception:
					continue



		sort_tweet = sorted(retweet_map, key=retweet_map.get, reverse=True)
		return sort_tweet[:4]


	def aggregate_photos(self, screen_name, count):
		if not self.timeline:
			try:
				self.timeline = self.t.statuses.user_timeline(screen_name=screen_name, count=count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		photo_map = {}
		for tweet in self.timeline:
			if "media" in tweet["entities"]:
				if not tweet["text"].startswith('RT', 0, 2):
					media = tweet["entities"]["media"]
					for url in media:
						photo_map[url["media_url"]] = float(tweet["favorite_count"]) + float(tweet["retweet_count"])
		sort_map = sorted(photo_map, key=photo_map.get, reverse=True)
		return sort_map[:5]


	def get_following(self, screen_name):
		"""Returns user profiles for the most recent 100 friends
		(people a given user follows)."""
		friends = self.t.friends.list(screen_name=screen_name, count=100)
		return friends['users']


	def get_followers(self, screen_name):
		"""Returns user profiles for the most recent 100 followers."""
		followers = self.t.followers.list(screen_name=screen_name, count=100)
		return followers['users']
