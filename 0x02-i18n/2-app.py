#!/usr/bin/env python3
"""Flask app"""
from flask_babel import Babel
from flask import Flask, render_template
from flask import g, request


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ["en", "fr"]
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match for supported languages"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['fr', 'en'])


@app.route('/')
def home():
    """
    Render the home page with the specified HTML template
    """
    return render_template(
            "2-index.html", languages=app.config['LANGUAGES'],
            default_locale=app.config['BABEL_DEFAULT_LOCALE'],
            default_timezone=app.config['BABEL_DEFAULT_TIMEZONE']
            )


if __name__ == "__main__":
    app.run(debug=True)
