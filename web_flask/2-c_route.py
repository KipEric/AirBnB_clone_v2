#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


"""Function that retun hello hbnb"""
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


"""Function that return HBNB"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


"""Function that return c text"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
