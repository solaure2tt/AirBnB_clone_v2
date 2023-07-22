#!/usr/bin/python3
"""script that starts a Flask web application
   /: display “Hello HBNB!”
   /hbnb: display “HBNB”"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """function that display “Hello HBNB!”"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello2():
    """function that display HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
