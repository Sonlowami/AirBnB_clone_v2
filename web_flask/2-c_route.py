#!/usr/bon/python3
"""
This module contain a WSGI flask application
"""
from flask import Flask
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
def print_param(text):
    """Return the parameter passed in a text"""
    new_text = text.replace('_', ' ')
    return f"C {escape(new_text)}\n"


app.run(host="0.0.0.0", port=5000)
