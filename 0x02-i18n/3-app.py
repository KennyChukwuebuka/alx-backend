#!/usr/bin/env python3
"""
    Flask App
"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    return render_template('3-index.html',
                           title=_('home_title'), header=_('home_header'))


if __name__ == '__main__':
    app.run()
