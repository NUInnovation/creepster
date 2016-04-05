# app.py
from flask import Flask

app = Flask(__name__, static_url_path='')

@app.route('/hello')
def hello():
	return 'Hello world!'

@app.route('/')
def root():
	return app.send_static_file('index.html')


if __name__ == '__main__':
	app.run()
