#!/usr/bin/python3
"""
This module contain a WSGI flask application that reads data from a storage
engine and display on the templates
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask('web_flask')


@app.teardown_appcontext
def close(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """Return a list of states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
