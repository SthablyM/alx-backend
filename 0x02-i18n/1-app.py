#!/usr/bin/env python3
"""class that has a LANGUAGES class attribute"""
from flask import Flask, render_template
from flask import g, request
from flask_babel import Babel
from datetime import datetime


class Config:
    """Configuration of available language"""
    LANGUAGES = {"en": "English", "fr": "French"}


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """the locale from the user settings"""
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


@app.route('/')
def home():
    """Render the home page with the specified HTML template."""
    return render_template("1-index.html", utc_time=utc_now)


if __name__ == "__main__":
    app.run(debug=True)
