from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself', validators=[Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField("Title",validators=[Required()])
    body = TextAreaField("Blog", validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField("Your Name")
    comment_body = StringField("Comment",validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    name = StringField("Your Name")
    email = StringField("Email")
    submit= SubmitField('Subscribe')

# class LoginForm(FlaskForm):
#     name = StringField("Your Name")
#     email = StringField("Email")
#     password = StringField("Password")
#     submit= SubmitField('Subscribe')
