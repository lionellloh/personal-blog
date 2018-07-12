from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

# Below are some DB methods

    @property
    def password(self):
        raise AttributeError('Password cannot be accessed')

    @password.setter
    def password(self,password):
        self.password_hash  = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)

    def __repr__(self):

        return 'User:{}'.format(self.username)

# Set up user_loader

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), index = True)
    draft = db.Column(db.Text())
    content = db.Column(db.Text())
    post_timestamp = db.Column(db.DateTime())
    edit_timestamp = db.Column(db.DateTime())
    view_num = db.Column(db.Integer())
    users = db.relationship('User', backref='users',
                            lazy='dynamic')

    def __repr__(self):
        return "Post: {}".format(self.title)




