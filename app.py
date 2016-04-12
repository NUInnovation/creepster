# app.py
from flask import Flask, request, render_template
import search_twitter

app = Flask(__name__, static_url_path='/static')

@app.route('/hello')
def hello():
	return 'Hello world!'

@app.route('/')
def root():
	return render_template('home.html')

@app.route('/profile', methods=['POST'])
def search():
	name = request.form['search']
	screen_name = search_twitter.search_username(name)
	twitter_loc = search_twitter.user_location(screen_name)
	twitter_des = search_twitter.user_description(screen_name)
	hashtags = search_twitter.aggregate_hashtags(screen_name, 3200)
	retweet = search_twitter.aggregate_retweets(screen_name, 3200)
	return render_template('profile.html', search=name, hashtags=hashtags, retweet=retweet, t_loc=twitter_loc, t_desc=twitter_des)


if __name__ == '__main__':
	app.run()
