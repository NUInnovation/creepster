# app.py
from flask import render_template, request
import json

from app import app

from app.clients.instagram_client import InstagramClient
from app.clients.geolocation_client import GeolocationClient
from app.clients.spotify_client import SpotifyClient
from app.clients.twitter_client import TwitterClient
from app.clients.youtube_client import YoutubeClient
from app.exceptions.media_missing_exception import MediaMissingException
from app.exceptions.no_locations_exception import NoLocationsException
from app.exceptions.no_twitter_account_exception import NoTwitterAccountException
from app.exceptions.rate_limit_exception import RateLimitException
from app.services.user_network_service import UserNetworkService

@app.route('/hello')
def hello():
	return 'Hello world!'


@app.route('/')
def root():
	return render_template('home.html')


@app.route('/profile', methods=['POST'])
def search():

	# get twitter data
	twttr = TwitterClient()
	name = request.form['search']
	no_twitter = False
	screen_name = ''
	twitter_loc = ''
	twitter_des = ''
	hashtags = []
	retweet = []
	photo = []
	profile =[]
	links = []
	t_stats = {}
	animals = {}
	verified_followers = []
	verified_following = []
	try:
		screen_name = twttr.search_username(name)
		data = twttr.fetch_data(screen_name, 1000, ["itunes", "spotify", "sptfy", 'youtube'], ["cat", "dog", "puppy", "kitten", "puppies"])
		twitter_loc = data["location"]
		twitter_des = data["description"]
		hashtags = data["hashtags"]
		retweet = data["retweet"]
		photo = data["photos"]
		p_url = twttr.get_user_profile(screen_name)["profile_image_url_https"]
		profile =  [] if "default_profile_images" in p_url else p_url
		links = data["links"]
		t_stats = data["stats"]
		animals = data["keyword_search"]
		verified_followers = twttr.get_verified_followers(screen_name)[:5]
		verified_following = twttr.get_verified_following(screen_name)[-5:]
	except NoTwitterAccountException:
		no_twitter = True

	# get instagram data
	user_network = UserNetworkService(screen_name)
	insta = InstagramClient()
	geolocation = GeolocationClient()
	search_term = request.form['search']
	username = ''
	media_missing = False
	no_locations = False
	rate_limited = False
	markers = []
	i_stats = {}
	insta_photos = []
	try:
		username = user_network.get_best_instagram_username()
		location_names = insta.get_location_names(username)
		for location in location_names:
			current_marker = {'title': location}
			coordinates = geolocation.find_coordinates(location)
			if coordinates:
				current_marker.update(coordinates)
				markers.append(current_marker)
		insta_photos = insta.aggregate_photos(username)
		insta_prof = insta.get_user_profile_picture(username)
		profile = profile if not insta_prof else insta_prof
		i_stats = insta.get_instagram_stats(username)
	except MediaMissingException:
		media_missing = True
	except NoLocationsException:
		no_locations = True
	except RateLimitException:
		rate_limited = True

	# split spotify urls
	spotify_uris = []
	if 'spotify' in links:
		spotify = SpotifyClient(links['spotify'])
		spotify_uris = spotify.generate_uris()

	# split youtube urls
	youtube_uris = []
	if 'youtube' in links:
		youtube = YoutubeClient(links['youtube'])
		youtube_uris = youtube.generate_uris()

	# grab names of verified followers/following
	verified_follower_names = [follower['name'] for follower in verified_followers]
	verified_following_names = [following['name'] for following in verified_following]

	# render template with template variables
	return render_template(
		'profile.html',
		search=name,
		hashtags=hashtags,
		retweet=retweet,
		t_loc=twitter_loc,
		t_desc=twitter_des,
		t_pic=photo,
		i_pic=insta_photos,
		markers=json.dumps(markers),
		media_missing=media_missing,
		no_locations=no_locations,
		no_twitter=no_twitter,
		rate_limited=rate_limited,
		profile=profile,
		spotify_uris=spotify_uris,
		youtube_uris=youtube_uris,
		t_stats=t_stats,
		i_stats=i_stats,
		animals=animals,
		verified_followers=verified_follower_names,
		verified_following=verified_following_names
	)


@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
	return render_template('home.html')


@app.route('/autocomplete', methods=['POST'])
def autocomplete():
	query = request.form['query']
	twitter = TwitterClient()
	usernames = twitter.search_usernames(query)
	return json.dumps(usernames)
