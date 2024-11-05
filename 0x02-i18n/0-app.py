#!/usr/bin/env python3
""" Basic flask app setup """
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    """ Render a template """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
