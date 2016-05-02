# 411_client.py
import os

import requests

class FourOneOneClient:
	def __init__(self):
		self.url = "https://proapi.whitepages.com/2.2/person.json?name="
		self.data = []

	# LIMIT API CALLS AS MUCH AS PHYSICALLY POSSIBLE
	def search(self, name):
		url = self.url+name.replace(" ", "+")
		response = requests.get(url+"&api_key=" + os.getenv('FOURONEONE_API_KEY')).json()
		self.data = response['results'][0]

	def get_addresses(self, name):
		if not self.data:
			self.search(name)
		addr = []
		for loc in self.data['locations']:
			addr.append(loc['standard_address_line1'])
		return addr

	def get_lat_longs(self, name):
		if not self.data:
			self.search(name)
		lat = []
		for loc in self.data['locations']:
			lat.append(loc['lat_long'])
		return lat
