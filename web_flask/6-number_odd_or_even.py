#!/usr/bin/python3
"""
This module contain a WSGI flask application
"""
from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def index():
    """
    Return a simple hello HBNB message
    """
    return "Hello HBNB!\n"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a simple HBNB message"""
    return "HBNB\n"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    """Return the parameter passed in a text"""
    new_text = text.replace('_', ' ')
    return f"C {escape(new_text)}\n"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python(text='is cool'):
    """Prints passed text, is cool if not passed"""
    new_text = text.replace('_', ' ')
    return f"Python {escape(new_text)}\n"


@app.route('/number/<n>', strict_slashes=False)
def print_number(n):
    """Print a n if is a number"""
    try:
        if isinstance(int(n), int):
            return f"{n} is a nummber\n"
    except:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """ Display an html page only if n is an integer"""
    try:
        if isinstance(int(n), int):
            return render_template('5-number.html', number=n)
    except:
        abort(404)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Display an html showing a number and it's odd or even status"""
    return render_template('6-number_odd_or_even.html', number=n)
app.run(host="0.0.0.0", port=5000)
