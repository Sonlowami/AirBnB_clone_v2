#!/usr/bon/python3
"""
This module contain a WSGI flask application
"""
from flask import Flask, abort
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


app.run(host="0.0.0.0", port=5000)
