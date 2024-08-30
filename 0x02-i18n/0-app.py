#!/usr/bin/python3
"""a basic Flask app
"""
from flask import (Flask, render_template)
app = Flask(__name__)


@app.route('/', strict_slashes=False)
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
