#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def home():
    """
    Render the home page with the specified HTML template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True,  port=5001)
