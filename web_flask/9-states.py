#!/usr/bin/python3
"""script that starts a Flask web application
   and listall States in the DB
   """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states2():
    """function that display all states"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def list_states_id(id):
    """function that display a state with id"""
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """Remove the session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
