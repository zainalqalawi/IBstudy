############### IMPORTS ##################################################
from models import Base, User, Sched, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
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
############### CREATE DATABASE ###########################################
engine = create_engine('sqlite:///project.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
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
############### USER FUNCTIONS ############################################
def create_user(username,secret_word):
    user = User(username=username)
    user.hash_password(secret_word)
    session.add(user)
    session.commit()

def get_user(username):
    return session.query(User).filter_by(username=username).first()

def get_user_id(id_num):
    return session.query(User).filter_by(id=id_num).first()
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
############### SCHEDULE FUNCTIONS #########################################
def create_sched(subjects, time):
    #define variables to use in algorithm
    part_time = 0
    t = int(time)
    #empty 2d array will be used to organize schedule
    sb = []

    #### DEFINES AMOUNT OF TIME ####
    if t > 2 or t == 2:
        part_time = t/3
        i = 3
    elif t < 2 and t > 0:
        part_time = t/2
        i = 2
    else:
        print('out of bounds')
        part_time = part_time * 60
    #################################

    #Takes subject from input into seperate variables
    s1 = subjects[0]
    s2 = subjects[1]
    s3 = subjects[2]
    s4 = subjects[3]
    s5 = subjects[4]
    s6 = subjects[5]
    
    week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    #Creates a 2d array of all subjects in order of the schedule (List inside a list)
    for w in week:
        if i == 3:
            sb.append([w,random.choice(subjects),random.choice(subjects),random.choice(subjects)])
            
        elif i == 2:
            sb.append([w,random.choice(subjects),random.choice(subjects)])
            
        else:
            break
    
    #Creates an instance according to time (2 or one subject per day)
    if i == 3:
        sun = Sunday(s1= sb[0][1], s2= sb[0][2], s3=sb[0][3])
        mon = Monday(s1= sb[1][1], s2= sb[1][2], s3=sb[1][3])
        tues = Tuesday(s1= sb[2][1], s2= sb[2][2], s3=sb[2][3])
        wed = Wednesday(s1= sb[3][1], s2= sb[3][2], s3=sb[3][3])
        thur = Thursday(s1= sb[4][1], s2= sb[4][2], s3=sb[4][3])
        fri = Friday(s1= sb[5][1], s2= sb[5][2], s3=sb[5][3])
        sat = Saturday(s1= sb[6][1], s2= sb[6][2], s3=sb[6][3])
    elif i == 2:
        sun = Sunday(s1= sb[0][1], s2= sb[0][2])
        mon = Monday(s1= sb[1][1], s2= sb[1][2])
        tues = Tuesday(s1= sb[2][1], s2= sb[2][2])
        wed = Wednesday(s1= sb[3][1], s2= sb[3][2])
        thur = Thursday(s1= sb[4][1], s2= sb[4][2])
        fri = Friday(s1= sb[5][1], s2= sb[5][2])
        sat = Saturday(s1= sb[6][1], s2= sb[6][2])

    #creates an instance for the basic schedule
    sched = Sched(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, time=part_time, real_time=t, i=i)

    #commits to the database
    session.add(sched)
    session.add(sun)
    session.add(mon)
    session.add(tues)
    session.add(wed)
    session.add(thur)
    session.add(fri)
    session.add(sat)
    session.commit()

def all_sched():
    return session.query(Sched).all()

#Gets schedule to display in home.html (found in app.py – home())
def get_sched(id_num):
    sun = session.query(Sunday).filter_by(id=id_num).first()
    mon = session.query(Monday).filter_by(id=id_num).first()
    tues = session.query(Tuesday).filter_by(id=id_num).first()
    wed = session.query(Wednesday).filter_by(id=id_num).first()
    thur = session.query(Thursday).filter_by(id=id_num).first()
    fri = session.query(Friday).filter_by(id=id_num).first()
    sat = session.query(Saturday).filter_by(id=id_num).first()
    
    #gets current users subjects
    user_sched = session.query(Sched).filter_by(id=id_num).first()

    if user_sched.i == 3:
        sched = [["Sunday", sun.s1, sun.s2, sun.s3], ["Monday", mon.s1, mon.s2, mon.s3], ["Tuesday", tues.s1, tues.s2, tues.s3], 
            ["Wednesday", wed.s1, wed.s2, wed.s3], ["Thursday", thur.s1, thur.s2, thur.s3], ["Friday", fri.s1, fri.s2, fri.s3], ["Saturday", 
            sat.s1, sat.s2, sat.s3]]
    else:
        sched = [["Sunday", sun.s1, sun.s2], ["Monday", mon.s1, mon.s2], ["Tuesday", tues.s1, tues.s2], ["Wednesday", wed.s1, wed.s2], [
            "Thursday", thur.s1, thur.s2], ["Friday", fri.s1, fri.s2], ["Saturday", sat.s1, sat.s2]]

    return sched
###########################################################################
