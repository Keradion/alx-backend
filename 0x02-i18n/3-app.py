#!/usr/bin/env python3
""" Basic flask app setup to implement i18n """
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Set default value for babel config variables """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match from our supported languages."""
    # Fetch locale from url parameter
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Render a template that display a text"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
