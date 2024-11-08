#!/usr/bin/env python3
""" Basic flask app setup to implement i18n """
from flask import Flask, render_template, request
from flask_babel import Babel, _

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
    """Force particular locale from locale parameter in the URLs."""
    # Fetch the value of locale parameter
    locale = request.args.get('locale')
    # Return locale if it founds in supported locale
    if locale in app.config['LANGUAGES']:
        return locale
    # Default behavior
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """ Render a template that display a text"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
