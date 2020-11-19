# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:22:23 2020

@author: tudor
"""
#from class_file import class_name
import os

from flask import Flask, render_template, request, flash, redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import RegisterForm, LoginForm #, MessageForm, UserUpdateForm
from models import db, connect_db, User



from werkzeug.exceptions import Unauthorized


CURR_USER_KEY = "curr_user"

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #Need this to be able to display flashing
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///springboard-trello"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "terces"


connect_db(app)
#db.drop_all()
#db.create_all()






@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)



@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    # IMPLEMENT THIS
    if CURR_USER_KEY in session:
        do_logout()
        flash(f"Hello,You have successfully logged out", "success")
        return redirect("/")

    else:
        flash("Not logged in to start with!.", 'danger')


@app.route("/" , methods = ['GET'])
def basic_display():
    
     return "Nothing here for now"