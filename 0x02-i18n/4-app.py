#!/usr/bin/env python3
"""task4"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']


@babel.localeselector
def get_locale():
    """
    the 'locale' parameter is in the request arguments and is supported
    """
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return requested_locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
