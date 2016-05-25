# __init__.py
from flask import Flask
import logging
import sys

app = Flask(__name__, static_url_path='/static')
# app.config.from_object('config')

# logging for Heroku
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

from app import views
