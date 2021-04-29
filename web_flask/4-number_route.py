#!/usr/bin/python3

"""
Script that starts a Flask web application:
- web appli must be listening on 0.0.0.0, port 5000
- Routes: /: display Hello HBNB!; /hbnb: display HBNB;
  /c/<text>: display C  followed by the value of the text variable
  (replace underscore _ symbols with a space );
- You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """returns HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """Display C followed by the value of the text variable"""
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_Python(text='is cool'):
    """Display Python, followed by the value of the text variable"""
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Display a number only if n is an integer"""
    return '%d is a number' % n

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
