# entitiy_recongnition_client.py
from context.nlp.entities import get_entities
from twitter_client import TwitterClient
from instagram_client import InstagramClient

class EntityRecongnitionClient:
	def __init__(self):
		self.TC = TwitterClient()
		self.IC = InstagramClient()

	def get_entities_from_tweets(self, screen_name, count):
		tweets = self.TC.search_tweets_for_user(screen_name, count)
		entities = []
		for tweet in tweets:
			ent = get_entities(tweet)
			for entry in ent:
				if entry["score"] >= 0.5:
					entities.append(entry)
		return entities

	def get_entities_from_instagram(self, screen_name):
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
		return entities




