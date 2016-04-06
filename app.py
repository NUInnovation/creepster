# app.py
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='static')

@app.route('/hello')
def hello():
	return 'Hello world!'

@app.route('/')
def root():
	# return app.send_static_file('index.html')
	return render_template('index.html')

@app.route('/profile', methods=['POST'])
def search():
	print(request.form['search'])
	return render_template('profile.html', search=request.form['search'])


if __name__ == '__main__':
	app.run()
