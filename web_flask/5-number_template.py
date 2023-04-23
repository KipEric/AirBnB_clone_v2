#!/usr/bin/python3
""" A script that starts a Flask web application"""


from flask import Flask, render_template
app = Flask(__name__)


"""Function to display hello hbnb"""
@app.route('/', strict_slashes=False)
def hello():
    return ('Hello HBNB!')


"""Function to display hbnb"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ('HBNB')


"""Function to display C"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return ('C {}'.format(text.replace('_', ' ')))


"""Function to display Python text"""
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return ('Python {}'.format(text.replace('_', ' ')))


"""Function to display integer number"""
@app.route('/number/int:n', strict_slashes=False)
def integer(n):
    return ('{} is a number'.format(n))


"""Function to display html page if number is an integer"""
@app.route('/number_temlate/<n>',strict_slashes=False)
def temp(n):
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
