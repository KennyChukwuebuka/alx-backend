#!/usr/bin/env python3
"""
    Flask App
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Retrieves a user based on a user id."""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determines the best match for supported languages."""
    # Check if the 'locale' argument is present in the request arguments
    locale = request.args.get('locale')

    # Verify if the locale is supported
    if locale in app.config['LANGUAGES']:
        return locale

    # Fallback to the default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Default route."""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
