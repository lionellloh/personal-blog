from flask import render_template, request, url_for, flash, redirect
from flask_login import login_required, current_user
from . import blog
from .forms import PostForm
from ..models import Post, User
from datetime import datetime
from app import db

@blog.route("/")

def blogposts():

    posts = Post.query.all()
    posts.reverse()


    return render_template('blog/index.html', title = "Blog", posts=posts)

@blog.route("/edit", methods =['GET', 'POST'])
@login_required

def add_post():
    form = PostForm()

    if form.validate_on_submit():

        post = Post(title = form.title.data,
                    content= form.content.data,
                    post_timestamp = datetime.now(),
                    author = current_user.first_name)
        try:
            db.session.add(post)
            db.session.commit()
            flash("Post added successfully")

        except:
            flash("Error: Post was not added")


        return redirect(url_for("blog.blogposts"))
    return render_template('blog/edit.html',
                           title = "Write Posts",
                           form = form)
