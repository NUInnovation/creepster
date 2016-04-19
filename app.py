# app.py
import json

from flask import Flask, request, render_template

from instagram_client import InstagramClient
from geolocation_client import GeolocationClient
from twitter_client import TwitterClient

app = Flask(__name__, static_url_path='/static')

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
	screen_name = twttr.search_username(name)
	twitter_loc = twttr.user_location(screen_name)
	twitter_des = twttr.user_description(screen_name)
	hashtags = twttr.aggregate_hashtags(screen_name, 3200)
	retweet = twttr.aggregate_retweets(screen_name, 3200)
	photo = twttr.aggregate_photos(screen_name, 1000)

	# get instagram data
	insta = InstagramClient()
	geolocation = GeolocationClient()
	search_term = request.form['search']
	username = insta.get_username(search_term)
	insta_photos = insta.aggregate_photos(username)
	photo.extend(insta_photos)
	location_names = insta.get_location_names(username)
	markers = []
	for location in location_names:
		current_marker = {'title': location}
		coordinates = geolocation.find_coordinates(location)
		if coordinates:
			current_marker.update(coordinates)
			markers.append(current_marker)

	# render template with template variables
	return render_template(
		'profile.html',
		search=name,
		hashtags=hashtags,
		retweet=retweet,
		t_loc=twitter_loc,
		t_desc=twitter_des,
		t_pic=photo,
		markers=json.dumps(markers)
	)


@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)
