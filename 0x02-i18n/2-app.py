#!/usr/bin/env python3
""" Basic flask app setup """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Set default value for babel config variables """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match from our supported languages."""
    return request.accept_langauges.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ Render a template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
