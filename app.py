from flask import Flask
# import tweepy
# from flask_sqlalchemy import SQLAlchemy


# Instantiate SQL database
server = Flask(__name__)
# db = SQLAlchemy(server)

# Instiantiate Flask application
app = Flask(__name__)


@app.route('/')
def landingPage():
    return '<p>This is the landing page.</p>'

# Terminal command to run:
# FLASK_APP=app.py flask run
# flask --app app run

# lang = en
# created_at
