############### IMPORTS ##################################################
#### DATABASE ####
from models import User, Sched
from database import *
#### Flask imports and functionalities
from flask import Flask, request, redirect, render_template
from flask import session as login_session
#### imports for algorithms
import array
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
############### initialize app ############################################# 
app = Flask(__name__)
# create secret key to protect the program security
app.config['SECRET_KEY'] = 'you-will-never-guess'
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
############### LOGIN & SIGNUP #############################################
@app.route('/')
def start():
    # opens start.html when the route is at defualt
    return render_template('start.html')

@app.route('/', methods=['POST'])
def login():
    # define user as the given username in the login form in start.html
    user = get_user(request.form['username'])
    # checks if the user exists and is matched with the right password
    if user != None and user.verify_password(request.form["password"]):
        #loggs user in my creating the current session for the user True
        login_session['name'] = user.username
        login_session['logged_in'] = True
        #Takes the user to their homepage
        return home()
    #if the user or password is incorrect, the page will be reset
    else:
        return render_template('start.html')

@app.route('/signup', methods=['POST', 'GET'])
#If the user is routed to /signup, they will GET the signup page, followed with the function signup after Posting the form. 
def signup(): 
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        # creates new user in the database User
        create_user(request.form['username'],request.form['password'])
        return render_template("setup.html")


@app.route('/logout')
def logout():
    # loggs user out if route lougout is called
    login_session['logged_in']= False
    return start()
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
############### CREATE NEW SCHEDULE #######################################
@app.route("/setup", methods =['GET', 'POST'])
def setup():
    if request.method == 'GET':
        return render_template("setup.html")

    else:
        # Recieves form data for the schedule and creates a list of the subjects
        s = [[request.form['s1'],request.form['level1'],request.form['score1'],request.form['priority1']],
        [request.form['s2'],request.form['level2'],request.form['score2'],request.form['priority2']],
        [request.form['s3'],request.form['level3'],request.form['score3'],request.form['priority3']],
        [request.form['s4'],request.form['level4'],request.form['score4'],request.form['priority4']],
        [request.form['s5'],request.form['level5'],request.form['score5'],request.form['priority5']],
        [request.form['s6'],request.form['level6'],request.form['score6'],request.form['priority6']]]
        t = request.form.get('time', False)

        #calls function to create the schedule from database.py
        create_sched(s, t)
        return start()
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
############### LOGGED-IN USER #############################################
@app.route("/home")
def home():
    #defines user with current user
    user=get_user(login_session['name'])
    #gets user id
    id_num = user.id
    #defines sched as the instance of the current user's study schedule
    sched = get_sched(id_num)
    #gets current users subjects
    user_sched = session.query(Sched).filter_by(id=id_num).first()
    #returns variables to html file
    return render_template("home.html", sched=sched, user_sched=user_sched)

@app.route("/setting")
def settings():
    return render_template("settings.html")
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
if __name__ == '__main__':
   app.run()
