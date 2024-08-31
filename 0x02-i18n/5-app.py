#!/usr/bin/env python3
"""
Babel setup
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """
    Config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    function, detect if the incoming request contains
    locale argument and ifs value is a supported locale,
    return it. If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.context_processor
def inject_globals():
    """
    Injects global variables into Jinja templates
    """
    return dict(get_locale=get_locale)


def get_user() -> dict:
    """
    Returns a user dictionary or None
    if the ID cannot be found or if
    the dictinary is empty
    """
    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Before each request, set the user's locale."""
    g.user = get_user()


@app.route("/")
def index() -> str:
    """
    This function renders the
    1-index.html file
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
