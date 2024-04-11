#!/usr/bin/env python3
"""A Basic Flask app with internationalization support.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    # Check if the 'locale' parameter is present in the request URL
    if 'locale' in request.args:
        # Retrieve the value of the 'locale' parameter
        requested_locale = request.args['locale']
        # Check if the requested locale is supported
        if requested_locale in app.config["LANGUAGES"]:
            return requested_locale
    
    # If the 'locale' parameter is not present or its value is not supported,
    # resort to the previous default behavior
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
