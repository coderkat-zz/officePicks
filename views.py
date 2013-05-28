from flask import Flask, render_template, redirect, request
from flask import session, g, flash, url_for
import os
from model import session as db_session, Admin, Series, Participant, Game
from localsettings import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.before_request
def load_user_id():
    g.user_id = session.get('user_id')


@app.route("/")
def index():
    # index page includes intro, login + signup
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
