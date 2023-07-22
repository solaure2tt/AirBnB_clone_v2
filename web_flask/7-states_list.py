#!/usr/bin/python3
"""script that starts a Flask web application
   and listall States in the DB
   """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """function that display all states"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def removesession():
    """Remove the session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
