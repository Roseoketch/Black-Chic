from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin #This helps us not to have to implement the method ourselves
from datetime import datetime
from . import login_manager
@login_manager.user_loader #modifies the load_user function by passing in a user_id to the function that queries the database and gets a User with that ID
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin, db.Model):
    """
    Defining the user object
    Creating new users
    db.Model connects class to our database to allow communication
    """
    __tablename__ = 'users'
#a singleuser represents a row in the table so we create columns using db.Column (db.Column represents a single column)
#db.Integer/string specifies the data in the column
#every row must have a primary key set to it
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), index = True)
    email= db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255)) #users biography
    blog = db.relationship("Blog", backref="user", lazy="dynamic")
    comment = db.relationship("Comment", backref="user", lazy="dynamic")
# storing hashes of passwords instead of passwords keeps users information secure
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        """
        Takes the user password, hashes it and stores it in  password_hash
        """
        self.password_hash = generate_password_hash

    def verify_password(self, password):
        """
        Compares users password to users password to verify validity
        """
        return check_password_hash(self.password_hash, password)

#  The @property decorator to create a a write only class property password.
# AttributeError blocks access to password property
#the below helps in debugging
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    """
    Defining the blog object
    """
    __tablename__='blogs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    author = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.relationship("Comment", backref="blogs", lazy="dynamic")
# db.relationship creates a virtual column that connects with the foreign key.
# We pass in 3 arguments. The first one is the class that we are referencing which is Comments.
# Next backref allows us to access and set our User class we give it the value of blogs now when we want to get the role of a user instance we can just run user.blogs.
# Lazy parameter is how SQLAlchemy will load our projects. The lazy option is our objects will be loaded on access and filtered before returning.
# save blogs
    def save_blogs(self):
        """
        Function that saves a blog category
        """
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_blogs(cls):
        """
        Function that returns all the data from the categories after being queried
        """
        blogs = Blog.query.all()
        return blogs

    @classmethod
    def clear_blogs(cls):
        """
        Function that clear all the blogs in a particular category
        """
        Blog.all_blogs.clear()
    all_blogs = []
    def __init__(self,
                title,
                body,
                author,
                users):
        self.title = title
        self.body = body
        self.author = author
        self.users = users

class Comment(db.Model):
    """
    Comment class that creates instances of Comment that will be attached to a particular blog
    """
    __tablename__='comment'

    # add columns
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blogs_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    def save_comment(self):
        """
        Saves the comment per blog
        """
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_comments(cls):
        comments =  Comment.query.all()
        return comments
    all_comments = []
    def __init__(self,
                comment,
                user):
        self.comment = comment
        self.user = user
# __init__ is the constructor for a class. The self parameter refers to the instance of the object. is what is called as a constructor in other OOP languages
#  the self variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter
# Setting those variables as self._x and self._y sets those variables as members of the Point object (accessible for the lifetime of the object).

class Subscribe(db.Model):
    # all_subscription = []
    __tablename__='subscribe'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    email=db.Column(db.String(255))

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_subscribers(cls):
        subscribers=Subscribe.query.all()
        return subscribers
