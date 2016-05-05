# entitiy_recongnition_client.py
from context.nlp.entities import get_entities
from twitter_client import TwitterClient
from instagram_client import InstagramClient
import wikipedia
import requests 
import urllib

class EntityRecongnitionClient:
	def __init__(self):
		self.TC = TwitterClient()
		self.IC = InstagramClient()
		self.t_entities = None
		self.i_entities = None
		self.music = ["singer", "songwriter", "recording artist", "musician", "vocalist", "band", "player"]

	def get_entities_from_tweets(self, screen_name, count):
		if self.t_entities:
			return self.t_entities
		tweets = self.TC.search_tweets_for_user(screen_name, count)
		entities = []
		for tweet in tweets:
			ent = get_entities(tweet)
			for entry in ent:
				if entry["score"] >= 0.5:
					entities.append(entry)
		self.t_entities = entities
		return self.t_entities 

	def get_entities_from_instagram(self, screen_name):
		if self.i_entities:
			return self.i_entities
		media = self.IC.get_user_media(screen_name)
		captions = []
		for photo in media["items"]:
			captions.append(photo["caption"]["text"])
		entities = []
		for caption in captions:
			ent = get_entities(caption)
			for entry in ent:
				if entry["score"] >= 0.5:
					entities.append(entry)
		self.i_entities = entities
		return self.i_entities

	def get_people(self, sn_twitter, sn_instagram):
		insta = self.get_entities_from_instagram(sn_instagram)
		twttr = self.get_entities_from_tweets(sn_twitter, 100)
		people = []
		for ent in insta:
			if ent["type"] == 'PERSON':
				if " " in ent["name"]:
					people.append(ent["name"])
		for ent in twttr:
			if ent["type"] == 'PERSON':
				if " " in ent["name"]:
					people.append(ent["name"])
		return people

	def search_wikipedia(self, query):
		page = wikipedia.search(query)
		if page:
			return wikipedia.summary(page[0], sentences=1)

	def get_musicians(self, sn_twitter, sn_instagram):
		people = self.get_people(sn_twitter, sn_instagram)
		musicians = []
		for person in people:
			desc = self.search_wikipedia(person)
			if any(terms in desc for terms in self.music):
				musicians.append(person)
		return musicians



