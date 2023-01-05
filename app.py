# from flask import Flask
# import tweepy
# from flask_sqlalchemy import SQLAlchemy

# # Instantiate SQL database
# server = Flask(__name__)
# db = SQLAlchemy(server)

# # Instiantiate Flask application
# app = Flask(__name__)


# @app.route('/')
# def landingPage():
#     return '<p>This is the landing page.</p>'

# # Terminal command to run:
# # FLASK_APP=app.py flask run
# # flask --app app run

# # lang = en
# # created_at
import math


def isPrime(n: int) -> bool:
    if n > 1:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    return False


def bigList() -> list:
    result = []
    for i in range(2, 1000001):
        if isPrime(i):
            result.append(i)
    return result


def bigListStr(arr: list) -> str:
    if len(arr) <= 15:
        return str(arr)
    result = '['
    for i in range(0, len(arr), 15):
        result += f'{str(arr[i:i+15])[1:-1]},\n'
    return result + ']'


with open('list2.txt', 'w') as f:
    f.write(str(bigListStr(bigList())))
