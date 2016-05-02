# run.py

import json
import os
import sys

def set_environment_vars():
    """Sets environment variables from a config.json file in the root directory.
    If the file is not found, an error message is printed."""
    try:
        config_file = open('config.json', 'r')
    except IOError:
        # catch missing file or other IOError
        print 'ERROR: config.json not found in root directory!'
        sys.exit()

    config_json = json.load(config_file)
    for key, value in config_json.iteritems():
        os.environ[key] = value


from app import app
set_environment_vars()
app.run(host='0.0.0.0', port=5000, debug=True)
