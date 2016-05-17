# twitter_client.py

#!/usr/bin/python
import json
import os

# from twitter import *
import twitter
from app.exceptions.no_twitter_account_exception import NoTwitterAccountException
from app.exceptions.rate_limit_exception import RateLimitException

class TwitterClient:
	def __init__(self):
		self.t = twitter.api.Twitter(auth=twitter.OAuth(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'), os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET')))
		self.timeline = None

	def fetch_data(self, screen_name, count, link_query, tweet_query):
		if not self.timeline:
			try:
				self.timeline = self.download_timeline(screen_name, count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		hashtag_map = {}
		retweet_map = {}
		sorted_photos = []
		links = {}
		kwd_output = {}
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
			if 'media' in tweet['entities']:
				if not tweet['text'].startswith('RT', 0, 2):
					media = tweet['entities']['media']
					for url in media:
						sorted_photos.append({
							'image_url': url['media_url'],
							'tweet_url': url['expanded_url'],
							'favorites': tweet['favorite_count'],
							'retweets': tweet['retweet_count']
						})

			if "urls" in tweet["entities"]:
				for urls in tweet["entities"]["urls"]:
					for query in link_query:
						if query in urls["expanded_url"]:
							if query not in links:
								links[query] = [urls['expanded_url']]
							else:
								links[query].append(urls["expanded_url"])

			for query in tweet_query:
				if query in tweet["text"]:
					if not query in kwd_output:
						kwd_output[query] = [tweet]
					else:
						kwd_output[query].append(tweet)

			for hashtag in tweet["entities"]["hashtags"]:
				name = hashtag["text"]
				if not name in hashtag_map:
					hashtag_map[name] = 1
				else:
					hashtag_map[name] = hashtag_map[name] + 1

		sort_hash = sorted(hashtag_map, key=hashtag_map.get, reverse=True)
		sort_tweet = sorted(retweet_map, key=retweet_map.get, reverse=True)
		sorted_photos = sorted(sorted_photos, key=lambda photo: photo['favorites'] + photo['retweets'], reverse=True)
		return {"hashtags": sort_hash[:4],
		"retweet": sort_tweet[:4],
		"photos": sorted_photos[:8],
		"links": links,
		"keyword_search": kwd_output,
		"location": self.user_location(screen_name),
		"description": self.user_description(screen_name),
		"stats": self.get_twitter_stats(screen_name)}

	def download_timeline(self, screen_name, count):
		"""Download a user timeline and cache it locally (for now)."""
		filename = 'app/cache/' + screen_name + '.txt'
		try:
			with open(filename, 'r') as cache_file:
				self.timeline = json.load(cache_file)
		except IOError:
			self.timeline = self.t.statuses.user_timeline(screen_name=screen_name, count=count)
			with open(filename, 'w') as cache_file:
				json.dump(self.timeline, cache_file)

		return self.timeline


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


	def get_user_profile(self, screen_name):
		"""Returns a user profile given a screen_name."""
		profile = self.t.users.lookup(screen_name=screen_name)[0]
		return profile


	def search_tweets_for_user(self, screen_name, count):
		if not self.timeline:
			try:
				self.timeline = self.download_timeline(screen_name, count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		text = []
		for tweet in self.timeline:
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
				self.timeline = self.download_timeline(screen_name, count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		for tweet in self.timeline:
			if tweet["place"] != None:
				print tweet["place"]


	def aggregate_hashtags(self, screen_name, count):
		if not self.timeline:
			try:
				self.timeline = self.download_timeline(screen_name, count)
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
				self.timeline = self.download_timeline(screen_name, count)
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
				self.timeline = self.download_timeline(screen_name, count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')

		sorted_photos = []
		for tweet in self.timeline:
			if 'media' in tweet['entities']:
				if not tweet['text'].startswith('RT', 0, 2):
					media = tweet['entities']['media']
					for url in media:
						sorted_photos.append({
							'image_url': url['media_url'],
							'tweet_url': url['expanded_url'],
							'favorites': tweet['favorite_count'],
							'retweets': tweet['retweet_count']
						})

		sorted_photos = sorted(sorted_photos, key=lambda photo: photo['favorites'] + photo['retweets'], reverse=True)
		return sorted_photos[:8]


	def get_following(self, screen_name):
		"""Returns user profiles for the most recent 100 friends
		(people a given user follows)."""
		try:
			friends = self.t.friends.list(screen_name=screen_name, count=200)
		except twitter.api.TwitterHTTPError as e:
			# HTTP error occurred
			if e.response_data['errors'][0]['code'] == 88:
				raise RateLimitException('Twitter')
			else:
				return []

		return friends['users']


	def get_followers(self, screen_name):
		"""Returns user profiles for the most recent 100 followers."""
		try:
			followers = self.t.followers.list(screen_name=screen_name, count=200)
		except twitter.api.TwitterHTTPError as e:
			# HTTP error occurred
			if e.response_data['errors'][0]['code'] == 88:
				raise RateLimitException('Twitter')
			else:
				return []

		return followers['users']

	def search_links(self, screen_name, querys, count):
		"""Searches links in tweets via query"""
		if not self.timeline:
			try:
				self.timeline = self.download_timeline(screen_name, count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')
		links = {}
		for tweet in self.timeline:
			if "urls" in tweet["entities"]:
				for urls in tweet["entities"]["urls"]:
					for query in querys:
						if query in urls["expanded_url"]:
							if query not in links:
								links[query] = [urls['expanded_url']]
							else:
								links[query].append(urls['expanded_url'])

		return links

	def search_tweets(self, screen_name, querys, count):
		tweets = self.search_tweets_for_user(screen_name, count)
		output = {}
		for tweet in tweets:
			for query in querys:
				if query in tweet:
					if not query in output:
						output[query] = [tweet]
					else:
						output[query].append(tweet)
		return output

	def get_twitter_stats(self, screen_name):
		"""Compiles followers, number of tweets and following"""
		if not self.timeline:
			try:
				self.timeline = self.download_timeline(screen_name, count)
			except Exception:
				raise NoTwitterAccountException('Tweets are protected')
		return {
		'followers': self.timeline[0]["user"]["followers_count"],
		'tweets': self.timeline[0]["user"]["statuses_count"],
		'following': self.timeline[0]["user"]["friends_count"]}
