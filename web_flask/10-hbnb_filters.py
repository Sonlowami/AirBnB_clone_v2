#!/usr/bin/python3
"""
This script contain a WSGI Flask application that displays
the AirBnB clone static page and fills it with data
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask('web_flask', static_url_path='')


@app.teardown_appcontext
def close(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def list_states():
    """List all states in the storage engine"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           context={'states': states, 'amenities': amenities})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
