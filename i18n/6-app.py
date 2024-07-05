#!/usr/bin/env python3
"""
Route module for the API
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


def get_locale():
    """
    Determine the best match with our supported languages.
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)


@app.route('/', methods=['GET'])
def output_index() -> str:
    """
    route that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    return render_template('6-index.html')


class Config:
    """
    Config class for flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Return user dictionary if ID found or None if not found.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Executed before all other functions.
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
