#!/usr/bin/python3
"""a basic Flask app
"""
from flask import (Flask, render_template)
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """Route handler for the root URL ('/').

        This function is invoked when the root URL of
        the application is accessed. It renders and returns
        the HTML template '1-index.html'.

        Returns:
            str: The rendered HTML template '1-index.html'.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
