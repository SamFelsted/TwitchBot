import json 

d = open("data.json")
users = json.load(d)

#pay, min bonus, max bonus
jobList = {"teacher": [60, 10, 60], "developer": [100, 0, 10], "streamer": [10, 5, 1000], "pet sitter": [20, 20, 100], "gamer": [5, 0, 100], "artist":[10, 10, 200], "musican":[30, 20, 60], "mom":[10, 50, 60], "farmer":[30, 40, 50]}

def makeData(user):
    users[user] = {'cash' : 100, 'level' : 1,'xp': 1, 'inv' : [], 'job': 'none'}
    save()

def save():
    with open('data.json', 'w') as f:
        json.dump(users, f, indent=4)

def checkData(userName):
    if users.has_key(userName):
        return True    
    else:
        print("No data")
        return False

def profile(userName):
    level = users[userName]['level']
    cash = users[userName]['cash']
    job = users[userName]['job']
    return [userName, level, cash, job]

def changeMoney(username, amount):
    users[username]['cash'] += amount 
    save()
    print(users[username]['cash'])

def getJob(username, job):
    if jobList.has_key(job.lower()):
        users[username]["job"] = job.lower()
        save()
        return True
    else:
        return False









