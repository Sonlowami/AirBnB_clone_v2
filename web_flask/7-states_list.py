#!/usr/bin/python3
"""
This module contain a flask web application that fetches data from the
storage engine. The storage engine can be a File Storage or a Database.
This flask application is, however, not supposed to know which engine it
is using.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask('web_flask')


@app.teardown_appcontext
def close(self):
    """Close the session after every request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List states in the storage engine"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
