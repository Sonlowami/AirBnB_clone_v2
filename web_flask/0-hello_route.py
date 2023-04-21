#!/usr/bin/python3
"""
This module contain a WSGI flask application
"""
from flask import Flask

app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def index():
    """
    Return a simple HBNB message
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)