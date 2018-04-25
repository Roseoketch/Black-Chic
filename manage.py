#!/usr/bin/env python3.6
from app import create_app, db
from flask_script import Manager,Server
from app.models import User,Blog, Comment
from flask_migrate import Migrate, MigrateCommand

# We use flask-migrate extension to create database migrations

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
# Initialize the Migrate class and pass the app instance and the db SQLAlchemy instance. We then create a new manager command 'db' and pass in the MigrateCommand class.

@manager.command
def test():
   """
   Run unit Tests
   """
   import unittest
   tests = unittest.TestLoader().discover('tests')
   unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
   return dict(app=app, db=db, User=User, Blog=Blog, Comment=Comment)
# We import Blog, User and Comment classes and pass it into our shell context


if __name__== '__main__':
   manager.run()
