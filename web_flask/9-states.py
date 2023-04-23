#!/usr/bin/python3
"""
This script contain a flask WSGI application that fetches information
from the database
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask('web_flask')


@app.teardown_appcontext
def close(self):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<string:idt>', strict_slashes=False)
def list_states(idt=None):
    """Return a list of states in storage engine"""
    states = storage.all(State)
    if idt:
        try:
            state = states['State.{}'.format(idt)]
            return render_template('9-states.html', state=state)
        except KeyError:
            return render_template('9-states.html')
    else:
        return render_template('9-states.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
