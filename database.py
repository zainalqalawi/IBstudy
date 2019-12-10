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
        part_time = t/3 * 60
        i = 3
    elif t < 2 and t > 0:
        part_time = t/2 * 60
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
    sub = [s1,s2,s3,s4,s5,s6]
    score_reverse = [0,7,6,5,4,3,2,1]
    # order subjects according to criteria 
    sub2 =[]
    for s in sub:
        level_val = int(s[1])
        score_val = score_reverse[int(s[2])]
        priority_val = int(s[3])

        p_score = level_val + score_val + priority_val - 3

        sub2.append([s[0],p_score])

    #sort to three arrays (high, medium, low)
    high_p = []
    med_p = []
    low_p = []

    for s in sub2:
        if int(s[1]) >=7 and int(s[1]) <=10:
            high_p.append(s[0])
        elif int(s[1]) >=4 and int(s[1]) <=6:
            med_p.append(s[0])
        elif int(s[1]) >=1 and int(s[1]) <=3:
            low_p.append(s[0])
        else:
            break
    
    empty = []

    #Sort arrays (High, med, low) according to time
    high = len(high_p) - 1
    med = len(med_p) - 1
    low = len(low_p) - 1
    l = 0
    if i == 3:
        if med_p == empty and high_p == empty and low_p == empty:
            print ('error')
        elif med_p == empty and low_p == empty:
            for s in range(21):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
            l = 0
        elif high_p == empty and med_p == empty:
            for s in range(21):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
            l = 0
        elif high_p == empty and low_p == empty:
            for s in range(21):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0
            l = 0
        elif high_p == empty:
            for s in range(12):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0
            l = 0
            for s in range(9):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
            l = 0
        elif med_p == empty:
            for s in range(15):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
            l = 0
            for s in range(6):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
            l = 0
        elif low_p == empty:
            for s in range(12):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
            l = 0
            for s in range(9):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0
            l = 0
        else:
            for s in range(10):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
    
            l = 0
            for s in range(7):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0

            l = 0
            for s in range(4):
                sb.append(low_p[l])
                l = l + 1
                if l > low :
                    l = 0
        # randomize array
        random.shuffle(sb)

        sun = Sunday(s1= str(sb[0]), s2= str(sb[1]), s3= str(sb[2]))
        mon = Monday(s1= str(sb[3]), s2= str(sb[4]), s3= str(sb[5]))
        tues = Tuesday(s1= str(sb[6]), s2= str(sb[7]), s3= str(sb[8]))
        wed = Wednesday(s1= str(sb[9]), s2= str(sb[10]), s3= str(sb[11]))
        thur = Thursday(s1= str(sb[12]), s2= str(sb[13]), s3= str(sb[14]))
        fri = Friday(s1= str(sb[15]), s2= str(sb[16]), s3= str(sb[17]))
        sat = Saturday(s1= str(sb[18]), s2= str(sb[19]), s3= str(sb[20]))
        
    if i == 2:
        if med_p == empty and high_p == empty and low_p == empty:
            print ('error')
        elif med_p == empty and low_p == empty:
            for s in range(14):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
            l = 0
        elif high_p == empty and med_p == empty:
            for s in range(14):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
            l = 0
        elif high_p == empty and low_p == empty:
            for s in range(4):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0
            l = 0
        elif high_p == empty:
            for s in range(8):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0
            l = 0
            for s in range(6):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
            l = 0
        elif med_p == empty:
            for s in range(9):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
            l = 0
            for s in range(5):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
            l = 0
        elif low_p == empty:
            for s in range(8):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
            l = 0
            for s in range(6):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0
            l = 0
        else:
            for s in range(7):
                sb.append(high_p[l])
                l = l + 1
                if l > high:
                    l = 0
    
            l = 0
            for s in range(4):
                sb.append(med_p[l])
                l = l + 1
                if l > med:
                    l = 0

            l = 0
            for s in range(3):
                sb.append(low_p[l])
                l = l + 1
                if l > low:
                    l = 0
        # randomize array
        random.shuffle(sb)

        sun = Sunday(s1= sb[0], s2= sb[1])
        mon = Monday(s1= sb[2], s2= sb[3])
        tues = Tuesday(s1= sb[4], s2= sb[5])
        wed = Wednesday(s1= sb[6], s2= sb[7])
        thur = Thursday(s1= sb[8], s2= sb[9])
        fri = Friday(s1= sb[10], s2= sb[11])
        sat = Saturday(s1= sb[12], s2= sb[13])

    #creates an instance for the basic schedule
    sched = Sched(s1=s1[0], s2=s2[0], s3=s3[0], s4=s4[0], s5=s5[0], s6=s6[0], time=part_time, real_time=t, i=i)

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

def randomize_sched(id_num):
    sched = session.query(Sched).filter_by(id=id_num).first()

    
    

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
    time = str(user_sched.time) + ' mins per subject'

    if user_sched.i == 3:
        sched = [["Sunday", sun.s1, sun.s2, sun.s3, time], ["Monday", mon.s1, mon.s2, mon.s3, time], ["Tuesday", tues.s1, tues.s2, tues.s3, time], 
            ["Wednesday", wed.s1, wed.s2, wed.s3, time], ["Thursday", thur.s1, thur.s2, thur.s3, time], ["Friday", fri.s1, fri.s2, fri.s3, time], ["Saturday", 
            sat.s1, sat.s2, sat.s3, time]]
    else:
        sched = [["Sunday", sun.s1, sun.s2, time], ["Monday", mon.s1, mon.s2, time], ["Tuesday", tues.s1, tues.s2, time], ["Wednesday", wed.s1, wed.s2, time], [
            "Thursday", thur.s1, thur.s2, time], ["Friday", fri.s1, fri.s2, time], ["Saturday", sat.s1, sat.s2, time]]

    return sched
###########################################################################
