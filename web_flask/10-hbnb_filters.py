#!/usr/bin/python3
"""script that starts a Flask web application
   and listall cities by states in the DB
   """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def cities_states1():
    """function that display cities by states"""
    states = storage.all("State")
    return render_template('10-hbnb_filters.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
