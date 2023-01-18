# These are SQLAlchemy models for building the Tweet database.
# All I need for each Tweet are:
# 1) A unique ID
# 2) The text of the Tweet
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User#{}: {}>".format(self.id, self.text)
