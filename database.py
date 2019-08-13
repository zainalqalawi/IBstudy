from models import Base, User, Sched
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

#### CREATE DATABASE ####
engine = create_engine('sqlite:///project.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

#### USER FUNCTIONS ####
def create_user(username,secret_word):
    user = User(username=username)
    user.hash_password(secret_word)
    session.add(user)
    session.commit()

def get_user(username):
    return session.query(User).filter_by(username=username).first()

def get_user_id(id_num):
    return session.query(User).filter_by(id=id_num).first()
    
def create_sched(subjects, time):

    part_time = 0
    t = int(time)

    
    if t > 2 or t == 2:
        part_time = t/3

    elif t < 2 and t > 0:
        part_time = t/2

    else:
        print('out of bounds')
        part_time = part_time * 60

    s1 = subjects[0]
    s2 = subjects[1]
    s3 = subjects[2]
    s4 = subjects[3]
    s5 = subjects[4]
    s6 = subjects[5]
    
    sched = Sched(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, time=part_time, real_time=t)
    session.add(sched)
    session.commit()

def all_sched():
    return session.query(Sched).all()

def get_sched(id_num):
    return session.query(Sched).filter_by(id=id_num).first()