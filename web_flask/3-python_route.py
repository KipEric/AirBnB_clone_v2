#!/usr/bin/python3
""" A script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


"""Function that display Hello hbnb"""
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


"""Function that return hbnb"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


"""Function that return c text"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))


"""Function that return python is cool"""
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python(text):
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
