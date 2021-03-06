from flask import render_template, request
from flask_login import login_required

from . import home

@home.route('/')

def homepage():

    return render_template('home/index.html', title = "Welcome")

home.route('/')

@home.route('/about')
def about():

    return render_template('home/about.html', title = "About")

@home.route('/dashboard')

@login_required

def dashboard():

    return render_template('home/dashboard.html', title = "Dashboard")
