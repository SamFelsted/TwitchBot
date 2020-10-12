import json 

d = open("data.json")
users = json.load(d)


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

makeData("Joe")
makeData("AlphaZulu22")
save()
changeMoney('AlphaZulu22', 10)







