#!/usr/bin/python3
"""a basic Flask app
"""
from flask import (Flask, render_template)
app = Flask(__name__)


class Config:
    """Configuration class for Flask-Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Route handler for the root URL ('/').

        This function is invoked when the root URL of
        the application is accessed. It renders and returns
        the HTML template '0-index.html'.

        Returns:
            str: The rendered HTML template '0-index.html'.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
