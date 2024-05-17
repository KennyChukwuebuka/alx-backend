#!/usr/bin/env python3
'''Task 6: Use user locale
'''

from flask import Flask, request, g
from flask_login import current_user, login_user, UserMixin, LoginManager

app = Flask(__name__)

# Example configuration of supported languages
app.config['LANGUAGES'] = ['en', 'es', 'fr']
app.config['DEFAULT_LOCALE'] = 'en'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)


# Dummy user class
class User(UserMixin):
    def __init__(self, id, locale):
        self.id = id
        self.locale = locale


# Dummy user loader
@login_manager.user_loader
def load_user(user_id):
    # This should return the user object from your database
    # For demonstration purposes, we return a dummy user
    return User(user_id, 'es')  # Assuming 'es' as preferred locale


def get_user_locale():
    """
    get_user_locale function
    """
    if current_user.is_authenticated:
        return current_user.locale
    return None


def get_locale():
    """
    get_locale function
    """
    # 1. Check if the 'locale' argument is present in the request arguments
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Check user settings for locale
    user_locale = get_user_locale()
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    # 3. Fallback to the request headers
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    # 4. Use the default locale
    return app.config['DEFAULT_LOCALE']


@app.route('/')
def index():
    """
        Index
    """
    return f"Locale: {get_locale()}"


# Dummy route to simulate login
@app.route('/login/<user_id>')
def login(user_id):
    """
        Login
    """
    user = load_user(user_id)
    login_user(user)
    return 'Logged in as: ' + str(user.id)


if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
