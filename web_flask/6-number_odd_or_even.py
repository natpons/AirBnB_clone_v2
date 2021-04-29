#!/usr/bin/python3

"""
Script that starts a Flask web application:
- web appli must be listening on 0.0.0.0, port 5000
- Routes:
  /: display Hello HBNB!; /hbnb: display HBNB;

  /c/<text>: display C  followed by the value of the text variable

  /python/(<text>): display Python, followed by the value of the text variable
  the default value of text is is cool

  /number/<n>: display n is a number only if n is an integer

  /number_template/<n>: display a HTML page only if n is an integer:
  H1 tag: Number: n inside the tag BODY

  /number_odd_or_even/<n>: display a HTML page only if n is an integer:
  H1 tag: Number: n is even|odd inside the tag BODY

- Must use the option strict_slashes=False in your route definition
- Replace underscore _ symbols with a space
"""

from flask import Flask
from flask import render_template
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


@app.route('/number_template/', strict_slashes=False)
@app.route('/number_template/<int:n>', strict_slashes=False)
def show_htmlpage(n=None):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def show_odd_or_even(n=None):
    """Display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)

#    if n % 2 == 0:
#        return render_template('6-number_odd_or_even.html', n=n, eq='even')
#    else:
#        return render_template('6-number_odd_or_even.html', n=n, eq='odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
