# app.py
from flask import Flask, request, render_template
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
	twttr = TwitterClient()
	name = request.form['search']
	screen_name = twttr.search_username(name)
	twitter_loc = twttr.user_location(screen_name)
	twitter_des = twttr.user_description(screen_name)
	hashtags = twttr.aggregate_hashtags(screen_name, 3200)
	retweet = twttr.aggregate_retweets(screen_name, 3200)
	return render_template('profile.html', search=name, hashtags=hashtags, retweet=retweet, t_loc=twitter_loc, t_desc=twitter_des)

@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)
