#!/usr/bin/env python3

# Flask is a lightweight web app framework (whereas Django is heavyweight).

from flask import Flask
from flask import render_template

app = Flask(__name__)


# This annotation causes this function to handle / requests on the web server.
@app.route('/')
def hello_world():
    greeting = "Hello, player!"

    # You can use HTML templates to dynamically generate pages.
    # They have to go in the templates/ subdir.
    page = render_template("index.html", greeting=greeting)
    return page

if __name__ == '__main__':
    app.run()


