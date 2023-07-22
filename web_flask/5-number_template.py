#!/usr/bin/python3
"""script that starts a Flask web application
   /: display “Hello HBNB!”
   /hbnb: display “HBNB”
   /c/<text>: display “C ” followed by the value of the text variable
   /python/(<text>): display “Python ”,
   followed by the value of the text variable
   /number/<n>: display “n is a number” only if n is an integer
   /number_template/<n>: display a HTML page only if n is an integer
   """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """function that display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello2():
    """function that display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello3(text):
    """function that display text without underscore
       replace underscore by space
    """
    res = text.replace("_", " ")
    return "C {}".format(res)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello4(text="is cool"):
    """function that display Python text without underscore
       replace underscore by space
    """
    res = text.replace("_", " ")
    return "Python {}".format(res)


@app.route("/number/<int:n>", strict_slashes=False)
def hello5(n):
    """function that display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello6(n):
    """function that display “n is a number” only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
