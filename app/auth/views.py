from flask import render_template, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
from ..models import User
from .forms import LoginForm

from . import auth

@auth.route('/')

def blog():

    return render_template('blog/index.html', title = "Blog")

@auth.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)

            flash("Welcome {}. Login Successful!".format(user.first_name))

            return redirect(url_for('blog.write'))


        else:
            flash("Invalid password or username.")


    return render_template('auth/login.html', form=form, title = "Login")


@auth.route('/logout')

@login_required

def logout():
    logout_user()
    flash('You have been succesfully logged out')

    return redirect(url_for('auth.login'))
