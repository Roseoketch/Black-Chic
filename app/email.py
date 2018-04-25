from flask_mail import Message
from flask import render_template
from . import mail

Subject_pref = 'black chic'
Sender_email = 'lizzichanga@gmail.com'

def mail_message(subject,template,to,**kwargs):
    # sender_email = 'lizzichanga@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[user for user in to.slipt(',')])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)


def send_email(subject,template,to,**kwargs):
    sender_email = 'lizzichanga@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
