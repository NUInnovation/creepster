# run.py

import json
import os
import sys


def create_cache_folder():
    """Creates a folder in the 'app' directory to hold cached files if it
    does not already exist."""
    cache_directory = 'app/cache'
    if not os.path.exists(cache_directory):
        os.makedirs(cache_directory)


def set_environment_vars():
    """Sets environment variables from a config.json file in the root directory.
    If the file is not found, a warning message is printed."""
    try:
        config_file = open('config.json', 'r')
        config_json = json.load(config_file)
        for key, value in config_json.iteritems():
            os.environ[key] = value
    except IOError:
        # catch missing file or other IOError
        print 'WARNING: config.json not found in root directory!'


from app import app

if __name__ == '__main__':
    set_environment_vars()
    create_cache_folder()
    app.run(debug=True)
