#!/usr/bin/python3
""" A script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


"""A function to display Hello hbnb"""
@app.route('/', strict_slashes=False)
def hello():
    return ('Hello HBNB!')


"""Function to display hbnb text"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ('HBNB')


"""Function to display C is cool"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return ('C {}'.format(text.replace('_', ' ')))


"""Function to display python text"""
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return ('Python {}'.format(text.replace('_', ' ')))


"""Function to display an integer number"""
@app.route('/number/int:n', strict_slashes=False)
def integer(n):
    return ('{} is a number'.format(n))


"""Function to display html page if number is an integer"""
@app.route('/number_temlate/<n>',strict_slashes=False)
def temp(n):
    return render_template('5-number.html', number=n)


"""Function that displays html page only if number is an integer"""
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n, num='even')
    else:
        return render_template('6-number_odd_or_even.html', number=n, num='odd')


"""A function that display a HTML page"""
@app.route('/states_list', strict_slashes=False)
def states():
    return render_template('7-states_list.html', states=storage.all("State"))


"""Method that handle teardown context"""
@app.teardown_appcontext
def teardown_appcontex(err):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

