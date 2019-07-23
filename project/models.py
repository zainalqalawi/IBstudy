from project import db

from flask import request, redirect, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id             		   = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email          		   = db.Column(db.String, unique=True, nullable=False)
    password_hash  		   = db.Column(db.String, nullable=False)
    name          		   = db.Column(db.String, nullable=False)

    def __init__(self, email,name,password):
        self.email         = email
        self.set_password(password)
        self.name          = name

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.email)


class Sched(UserMixin, db.Model):

	id           			= db.Column(db.Integer, primary_key=True, autoincrement=True)
	classess  	 			= db.Column(db.Array, nullable=False)
	time      	 			= db.Column(db.Array, nullable=False)
	week     	 			= db.Column(db.Array, nullable=False)

	def __init__(self, classess, time, week):

		self.classess   	= classess
		self.time       	= time
		self.week       	= week
