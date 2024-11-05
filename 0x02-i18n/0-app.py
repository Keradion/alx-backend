#!/usr/bin/env python3
""" Basic flask app setup """
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    """ Render a template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
