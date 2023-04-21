#!/usr/bon/python3
"""
This module contain a WSGI flask application
"""
from flask import Flask

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


app.run(host="0.0.0.0", port=5000)
