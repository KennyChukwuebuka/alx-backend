#!/usr/bin/env python3
"""Instantiate babel object in the app and store it in a
    model-level variable named babel

    create a config class the has LANGUAGES class att ['en', 'fr']
    use config to set bable default locale ("en") and Timezone ("UTC")
    Use the class as config to flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
        Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=True)
def index():
    """
        Index
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
