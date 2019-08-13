from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class User(Base, UserMixin):

    __tablename__ = "users"

    id             		   = Column(Integer, primary_key=True)
    username          	   = Column(String)
    password_hash  		   = Column(String)

    def hash_password(self, password):
        self.password_hash = pwd_security.encrypt(password)
    def verify_password(self, password):
        return pwd_security.verify(password, self.password_hash)


    def __repr__(self):
        return 'User %d %s' % (self.id, self.username)

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

    def __repr__(self):
        return "Subjects: {} \n time:{} \n week: {}\n part_time {}".format(self.subjects, self.time, self.week, self.part_time)

class Sunday(Base):
    __tablename__           = "Sunday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

class Monday(Base):
    __tablename__           = "Monday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

class Tuesday(Base):
    __tablename__           = "Tuesday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

class Wednesday(Base):
    __tablename__           = "Wednesday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

class Thursday(Base):
    __tablename__           = "Thursday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

class Friday(Base):
    __tablename__           = "Friday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

class Saturday(Base):
    __tablename__           = "Saturday"
    id           			= Column(Integer, primary_key=True)
    s1  	 			    = Column(String)
    s2  	 			    = Column(String)
    s3  	 			    = Column(String)

    
    
                    