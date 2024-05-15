#!/usr/bin/env python3
"""
    Flask Application
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Define supported locales
SUPPORTED_LOCALES = ["en", "fr"]


@babel.localeselector
def get_locale():
    # Check if 'locale' parameter is present in the request
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale
    else:
        return request.accept_languages.best_match(SUPPORTED_LOCALES)


@app.route('/')
def index():
    return render_template('',
                           title=_('home_title'), header=_('home_header'))


if __name__ == '__main__':
    app.run()
