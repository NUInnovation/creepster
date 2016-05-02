# Creepster
### We Know Who You Are

## What is Creepster?
Creepster is an simple tool that takes a person's name and searches various social media and websites to find as much information on the person as possible. This can range from their address to which causes they publicly support. The purpose of Creepster is to make people aware of how much information they reveal about themselves online.

#### Currently Creepster searches:
* Twitter
* Instagram

#### Soon to be added:
* Pinterest
* 411


## Team Members
* Melanie Klerer
* Nevil George
* Joanne Lee
* Michael Bacos


## How to run locally
If you want to run Creepster on your computer, follow these steps:
* Clone the repo and install the dependencies (recommended: use a virtualenv)
```shell
git clone https://github.com/NUInnovation/creepster.git
pip install -r requirements.txt
```

* Create a file named config.json in the root directory using the config.example.json template and populate it with your secret keys.
```shell
python run.py
```

* Open https://localhost:5000 from your favorite browser
