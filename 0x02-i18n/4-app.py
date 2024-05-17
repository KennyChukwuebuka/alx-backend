#!/usr/bin/env python3
"""
    Flask Application
"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Dummy translations for demonstration purposes
def gettext(string):
    return {
        'Hello': 'Bonjour',
        'Welcome': 'Bienvenue',
        # Add more translations as needed
    }.get(string, string)

@app.route('/')
def index():
    greeting = _('Hello')
    welcome_message = _('Welcome to our website!')
    return render_template('4-index.html', greeting=greeting, welcome_message=welcome_message)

if __name__ == '__main__':
    app.run()
