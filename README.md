# Fetch (formerly Creepster)
### We Know Who You Are

## What is Fetch?
Fetch is an simple tool that takes a person's name and searches various social media and websites to find as much information on the person as possible. This can range from their address to which causes they publicly support. The purpose of Fetch is to make people aware of how much information they reveal about themselves online.

#### Currently Fetch searches:
* Twitter
* Instagram
* Spotify
* Youtube


## Team Members
* Melanie Klerer
* Nevil George
* Joanne Lee
* Michael Bacos


## How to run locally
Fetch uses Flask, a lightweight web framework written in Python. If you want to run Fetch on your computer, follow these steps:
* Clone the repo and install the dependencies (recommended: using a virtualenv)
```shell
git clone https://github.com/NUInnovation/creepster.git
pip install -r requirements.txt
```

* Create a file named config.json in the root directory using the config.example.json template and populate it with your secret keys

* Run the app
```shell
python run.py
```

* Open https://localhost:5000 from your favorite browser
