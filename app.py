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
	hashtags = search_twitter.aggregate_hashtags(search_twitter.search_username(name), 1000)
	return render_template('profile.html', search=name, hashtags=hashtags)

@app.route('/redirect', methods=['GET', 'POST'])
def redirect():
	return render_template('home.html')


if __name__ == '__main__':
	app.run()
