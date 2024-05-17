#!/usr/bin/env python3
"""
    Flask App
"""

from flask import Flask
from flask_babel import Babel
from flask_babel import lazy_gettext as _
from flask import render_template

app = Flask(__name__)
babel = Babel(app)

# Dummy translations for demonstration purposes
@babel.localeselector
def get_locale():
    return 'en'  # Return the desired default locale here

@app.route('/')
def index():
    greeting = _('Hello')
    welcome_message = _('Welcome to our website!')
    return render_template('3-index.html', greeting=greeting, welcome_message=welcome_message)

if __name__ == '__main__':
    app.run()
