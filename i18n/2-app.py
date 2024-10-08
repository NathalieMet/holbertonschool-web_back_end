#!/usr/bin/env python3
"""
Route module for the API
"""

from flask import Flask, render_template
from flask_babel import Babel
from flask import request


def get_locale():
    """
    Determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(['LANGUAGES'])


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def output_index():
    """
    route that simply outputs “Welcome to Holberton” as page title (<title>)
    and “Hello world” as header (<h1>).
    """
    return render_template('0-index.html')


class Config:
    """
    Config class for flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)
