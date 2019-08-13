#### DATABASE ####
from models import User, Sched
from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
import random
import array


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#### LOGIN ####
@app.route('/')
def start():
    return render_template('start.html')

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return home()
    else:
        return render_template('start.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    #check that username isn't taken
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        create_user(request.form['username'],request.form['password'])
        return render_template("setup.html")

@app.route('/logout')
def logout():
    login_session['logged_in']= False
    return start()
#### LOGIN END ####



@app.route("/setup", methods =['GET', 'POST'])
def setup():
    if request.method == 'GET':
        return render_template("setup.html")

    else:
        s1 = request.form.get('s1', False)
        s2 = request.form.get('s2', False)
        s3 = request.form.get('s3', False)
        s4 = request.form.get('s4', False)
        s5 = request.form.get('s5', False)
        s6 = request.form.get('s6', False)
        s = [s1,s2,s3,s4,s5,s6]
        t = request.form.get('time', False)

        create_sched(s, t)
        return start()


@app.route("/home")
def home():
    user=get_user(login_session['name'])
    id_num = user.id
    sched = get_sched(id_num)
    week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    s_list = [sched.s1, sched.s2, sched.s3, sched.s4, sched.s5, sched.s6]
    i = 0
    sb=[]

    if sched.real_time > 2 or sched.real_time == 2:
        i = 3
    elif sched.real_time < 2 and sched.real_time > 0:
        i = 2

    for w in week:
        if i == 3:
            sb.append([w,random.choice(s_list),random.choice(s_list),random.choice(s_list)])
            
        elif i == 2:
            sb.append([w,random.choice(s_list),random.choice(s_list)])
            
        else:
            break

    return render_template("home.html", sched=sb)

@app.route("/setting")
def settings():
    return render_template("settings")


if __name__ == '__main__':
   app.run(debug = True)
