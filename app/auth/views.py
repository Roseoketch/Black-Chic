from flask import render_template, redirect, request, url_for, flash
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm, RegistrationForm
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
   login_form = LoginForm() #instanciate LoginForm
   if login_form.validate_on_submit(): #check if valid
       user =  User.query.filter_by(email=login_form.email.data).first() #search for user using email
       if user is not None and  user.verify_password(login_form.password.data): #confirms hashed password
           login_user(user, login_form.remember.data) #record the user as logged for the current session
           return redirect(request.args.get('next') or url_for('main.index'))

       flash('Invalid username or Password')

   title = "Blog login"
   return render_template('auth/login.html', login_form=login_form, title=title)  #renders form in html

@auth.route('/register', methods=["GET", "POST"])
def register():
   form = RegistrationForm() #instanciate RegistationForm
   if form.validate_on_submit(): #check if valid
        user = User(email=form.email.data,
        username=form.username.data,
        password=form.password.data) #creates new user
        db.session.add(user)
        db.session.commit() #creates a row/column for this user

        return redirect(url_for('auth.login'))

        title = 'New Account'
   return render_template('auth/register.html', registratin_form=form, title=title) #renders form in html

@auth.route('/logout')
@login_required
def logout():
   logout_user()
   flash('You have successfully logged out')
   return redirect(url_for("main.index"))
# redirects user to the index page
