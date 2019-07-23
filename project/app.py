from flask import Flask 
app = Flask(__name__)


from project.models import User, Sched

@app.route('/')
def start():
	return render_template ('start.html')


@app.route("/setup")
def startup():




	
def schedule(time, classes, week):

	a = input("Enter your Group 1 subject: ")
    b = input("Enter your Group 2 subject: ")
    c = input("Enter your Group 3 subject: ")
    d = input("Enter your Group 4 subject: ")
    e = input("Enter your Group 5 subject: ")
    f = input("Enter your Group 6 or other subject: ")
    
    subjects = [a,b,c,d,e,f]
    t = input("How much time do you have to study per day (in hours): ")
    time = int(t)
    
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thurday", "Friday", "Saturday"]
    sbj = ["non"]
    part_time = 0
    i = 0
    
    if time > 2 or time == 2:
        part_time = time/3
        i = 3
    elif time < 2 and time > 0:
        part_time = time/2
        i = 2
    else:
        print('out of bounds')
    
    part_time = part_time * 60
    j = 0
    for x in week:
        if i == 3:
            print(week[j])
            print(random.choice(subjects), " for ", part_time, " minutes")
            print(random.choice(subjects), " for ", part_time, " minutes")
            print(random.choice(subjects), " for ", part_time, " minutes")
            j =+ 1
            
        elif i == 2:
            print(week[j])
            print(random.choice(subjects), " for ", part_time, " minutes")
            print(random.choice(subjects), " for ", part_time, " minutes")
            j =+ 1
            
        else:
            break




	# 1. if time is greater or equal to 2, equally seperate time into 3 parts + (optional for user) homework section for upcoming assignments
	# 2. if time is less than 2, seperate time into 2 parts + (optional for user) homework section for upcoming assignments
	# 3. Turn time into hours and mins 
	# 4. randomly gen classes with each time section time 
	# 5. repeat


