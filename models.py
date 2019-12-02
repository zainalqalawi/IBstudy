############### IMPORTS ##################################################
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.apps import custom_app_context as pwd_security
###########################################################################
#
#
#
#
#
#
#
#
#
#
############### DEFINE DB #################################################
Base = declarative_base()
###########################################################################
#
#
#
#
#
#
#
#
#
#
############### USER DATABASE #############################################
class User(Base, UserMixin):

    __tablename__ = "users"

    id             		   = Column(Integer, primary_key=True)
    username          	   = Column(String)
    password_hash  		   = Column(String)

    def hash_password(self, password):
        #encrypts password for security protection
        self.password_hash = pwd_security.encrypt(password)
    def verify_password(self, password):
        #verifies password through encryption 
        return pwd_security.verify(password, self.password_hash)

    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)
###########################################################################
#
#
#
#
#
#
#
#
#
#
############### SCHEDULE DATABASES #########################################
class Sched(Base):
    __tablename__           = "Schedule"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)
    s4  	 			    = Column(String)
    s5  	 			    = Column(String)
    s6  	 			    = Column(String)
    time      	 			= Column(Integer)
    part_time               = Column(Integer)
    real_time               = Column(Integer)
    i                       = Column(Integer)

    def __repr__(self):
        return "Subjects: {} \n time:{} \n week: {}\n part_time {}".format(self.subjects, self.time, self.week, self.part_time)

class Sunday(Base):
    __tablename__           = "Sunday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
class Monday(Base):
    __tablename__           = "Monday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

class Tuesday(Base):
    __tablename__           = "Tuesday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

class Wednesday(Base):
    __tablename__           = "Wednesday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

class Thursday(Base):
    __tablename__           = "Thursday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

class Friday(Base):
    __tablename__           = "Friday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

class Saturday(Base):
    __tablename__           = "Saturday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    def __repr__(self, s1='', s2='', s3=''):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
###########################################################################         