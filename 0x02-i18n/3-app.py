#!/usr/bin/env python3
"""task3"""
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@babel.localeselector
def get_locale():
    """determine the language"""
    return request.args.get('lang', 'en')


@app.route('/')
def home():
    """Render the home page with the specified HTML template"""
    return render_template('3-index.html')
