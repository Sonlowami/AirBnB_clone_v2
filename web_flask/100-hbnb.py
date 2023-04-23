#!/usr/bin/python3
"""
This module contain a Flask WSGI application that displays the full HBNB
web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place
from models.amenity import Amenity


app = Flask('web_flask')


@app.teardown_appcontext
def close(self):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def full_hbnb():
    """Display the full hbnb site"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
