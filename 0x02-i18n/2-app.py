#!/usr/bin/python3
"""A basic Flask application with internationalization
    support using Flask-Babel.

    This script sets up a Flask web application with localization support.
    It configures Flask-Babel to handle multiple languages and sets up
        a basic route for the root URL.

    Modules:
        - Flask: A web framework for building web applications.
        - Flask-Babel: An extension for Flask that adds i18n and l10n support.

    Classes:
        - Config: A configuration class for Flask-Babel settings.

    Functions:
        - get_locale: Determines the best match
            for the user's preferred language.

    Routes:
        - /: Handles requests to the root URL
            and renders the '2-index.html' template.
"""
from flask import Flask, render_template, request

from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get the current user default local
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """Route handler for the root URL ('/').

        This function is invoked when the root URL of
        the application is accessed. It renders and returns
        the HTML template '2-index.html'.

        Returns:
            str: The rendered HTML template '1-index.html'.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
