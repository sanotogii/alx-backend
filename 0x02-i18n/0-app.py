#!/usr/bin/env python3
"""
This script starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/0-index.html')
def hello_world() -> str:
    """
    This function renders the
    0-index.html file
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
