#!/usr/bin/env python3
"""
   Basic flask app setup to implement i18n
   The module helps to force locale based on the url
   parameter locale passed during http  request
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# To emulate a user login system
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Set default value for babel config variables """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.before_request
def before_request():
    """
       call get_user to find a user if any set it and
       a global on flask.g.user
    """
    user = get_user()
    g.user = user


def get_user():
    """
       Returns a user dictionary of None if the user id
       cannot be found or login_as was not passed in the url
    """
    # Fetch user_id from url parameter login_as
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    else:
        return None


@babel.localeselector
def get_locale():
    """To use a user’s preferred local if it is supported"""
    # (1) Locale From URL Parameter
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang

    # (2) Locale From user settings
    if g.user:
        locale = g.user.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # (3) Locale From request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Render a template that display a text"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
