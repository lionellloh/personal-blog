from flask import render_template, request

from . import blog

@blog.route("/")

def blog():

    return render_template('blog/index.html', title = "Blog")
