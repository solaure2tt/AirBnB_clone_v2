#!/usr/bin/python3
"""script that starts a Flask web application
   and listall States and their cities in the DB
   """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """function that display cities by states"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def removesession():
    """Remove the session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
