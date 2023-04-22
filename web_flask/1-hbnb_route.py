#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)

""" Function that return hello HBNB text"""
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


"""Function that return HBNB text"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
