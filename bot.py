import cfg
import ultis
import market

import random
import socket
import re 
import time
from time import sleep

canCommand = True
ms = cfg.messageSend
qst = cfg.questions
guns = cfg.guns
x = 0
y = 0
winChance = 0
pog = "backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG"
toby = "backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby"
mineCont = 0
def jobFormat(job, command):
    job = job.replace(command, "")
    job = job.replace("\r","")
    job = job.replace("\n","")
    print(job)
    return job.lower()

def main():
    global canCommand
    workedUsers = []
    global mineCont
    global winChance
    global x 
    global y
    s = socket.socket()
    s.connect(cfg.connection_data)
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))
    print(s)

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    #This goes to the functions and then to the char command
    ultis.chat(s, "Hello everyone!")
    while True: 
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n": 
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            #set x == 1 for 20 mins, x == 3 for thirty
            mineCont = 0
            print("mine reset")
            workedUsers[:] = []
            print("Work clean")
            if x == 1:
                print("Sending") 
                question = qst[random.randint(0, len(qst)- 1)] #Math is fun
                ultis.chat(s, question)
                x = 0
            elif y == 2:
                mess = ms[random.randint(0, len(ms)- 1)] #Math is fun
                ultis.chat(s, mess)
                y = 0
            else:
                x += 1
                y += 1
                print(x)
                print(y)
        else:
            username = re.search(r"\w+", response).group(0)
            username = username.lower()
            message = CHAT_MSG.sub("", response)
            print(response)

         #Custom Commands 0w0 
            if canCommand:
                #print(len(str(message)))
                #I should probably actaully do this command correctly, nahhhh
                if message.strip() == "!time":
                    #I really don't want to type a time command
                    canCommand = False
                    ultis.chat(s, "I don't know, you're the one on the computer, I'm just a program")
                    canCommand = True
                #about, aka me flexing I wrote this
                elif message.strip() == "!about":
                    canCommand = False
                    #sends the about
                    ultis.chat(s, cfg.about)
                    canCommand = True
                elif message.strip() == "!toby":
                    canCommand = False
                    ultis.chat(s, toby)
                    canCommand = True
            
                #Question Command
                elif message.strip() == "!question":
                    #sends a question 
                    canCommand = False
                    question = qst[random.randint(0, len(qst)- 1)] #Math is fun
                    ultis.chat(s, question)
                    canCommand = True
                #Nice
                elif "69" in message:
                    ultis.chat(s, "Nice")
                elif "who is joe?" in message.lower():
                    ultis.chat(s, "Joe Mama")
                #Roll a d6 command
                elif message.strip() == "!d6":
                    canCommand = False
                    diceRoll = random.randint(1, 6)
                    ultis.chat(s, diceRoll)
                    canCommand = True
                elif message.strip() == "!POG":
                    canCommand = False
                    ultis.chat(s, pog)
                    canCommand = True
                elif message.strip() == "!wholesome":
                    ultis.chat(s, "https://www.youtube.com/watch?v=IymCuWuqcXc")
                #Gun Command
                elif message.strip() == "!shoot":
                    canCommand = False
                    #Bang Bang Bang
                    gunMessage = "{} shoot a dummy with a{} and did {} points of damage".format(username, guns[random.randint(0, len(guns)- 1)],random.randint(0, 100))
                    ultis.chat(s, gunMessage)
                    canCommand = True
                elif message.strip() == "!chance":
                    canCommand = False
                    winChance = random.randrange(1, 101)
                    if username == "alphazulu22":
                        ultis.chat(s, "Sorry Alpha, no cuts for the programmer, but the win rate is {}%".format(winChance))
                    else:
                        ultis.chat(s, "The chance of the next fight starter winning is {}%".format(winChance))
                    canCommand = True
                elif "!fight" in message and len(str(message)) <= 60:
                    canCommand = False
                    if winChance == 0:
                        ultis.attack(s, username, message, 50)
                        print("Fair Match")
                    else:
                        ultis.attack(s, username, message, winChance)
                        winChance = 0
                    canCommand = True
                elif "!battle" in message and len(str(message)) <= 40:
                    canCommand = False
                    ultis.chat(s, "AlphaZulu22 has won and has slayed any challenger that dares to question this massive victory. He has delt 999,999,999 damage and healed for double that. He has a base life gen of 100,000 per nano sec and has a base health higher than infinity. He can not be slayed.")
                    canCommand = True
                #   Cool economy Commands

                elif message.strip() == "!profile":
                    canCommand = False
                    if market.checkData(username):
                        data = market.profile(username)
                        ultis.chat(s, username + ": ")
                        ultis.chat(s, " level: " + str(data[1]))
                        ultis.chat(s, " cash: $" + str(data[2]))
                        ultis.chat(s, " job: "  + str(data[3]))
                    else:
                        market.makeData(username)
                        ultis.chat(s, "No data was found, so a profile was made")
                    canCommand = True
                elif message.strip() == "!bal":
                    canCommand = False
                    if market.checkData(username):
                        data = market.profile(username)
                        ultis.chat(s, username + " has a balance of $" +  str(data[2]))
                    else:
                        market.makeData(username)
                        ultis.chat(s, "No data was found, so a profile was made")
                    canCommand = True
                elif message.strip() == "!mine":
                    canCommand = False
                    if market.checkData(username):
                        if mineCont <= 15:
                            mineCont += 1
                            chanceInt = random.randint(1, 100)
                            if chanceInt > 30:
                                ultis.chat(s, "Woah you went mining and found a diamond worth ${}".format(chanceInt))
                                market.changeMoney(username, chanceInt)
                            else:
                                ultis.chat(s, "Lol, you went mining and found nothing")
                        else:
                            ultis.chat(s, "The mine is empty right now please wait")
                    else: 
                        ultis.chat(s, "Make a profile with !profile to use this command")
                    canCommand = True
                elif "!getjob" in message and len(str(message)) <= 23:
                    canCommand = False
                    job = jobFormat(message, "!getjob ")
                    jobCheck = market.getJob(username, job)
                    if jobCheck and market.checkData(username):
                        ultis.chat(s, "Congrats you now have a job as a {}".format(job))
                    else:
                        ultis.chat(s, "Not a valid job or you have yet to set up your profile")
                    canCommand = True
                elif message.strip() == "!joblist":
                    canCommand = False
                    send = str(market.jobList.keys()).replace("'", "").replace("[", "").replace("]", "")
                    ultis.chat(s, "The jobs you can have are: " + send)
                    canCommand = True
                elif "!salary" in message and len(str(message)) <= 23:
                    canCommand = False
                    job = jobFormat(message, "!salary ")
                    if market.jobList.has_key(job):
                        salary = market.jobList[job]
                        ultis.chat(s, "The base salary of a {} is ${}, with a maxium bonus of ${}".format(job, salary[0], salary[2]))
                    else:
                        ultis.chat(s, "Not a valid job")
                    canCommand = True
                elif message.strip() == "!work":
                    canCommand = False
                    if market.checkData(username):
                        data = market.profile(username)
                        if data[3] != "none":
                            if username in workedUsers:
                                ultis.chat(s, "You're overworked man, try again in 15-20 mins")
                            else:
                                job = data[3]
                                pay = market.jobList[job][0]
                                low = market.jobList[job][1]
                                high = market.jobList[job][2]
                                bonus = random.randint(low, high)
                                market.changeMoney(username, pay + bonus)
                                ultis.chat(s, "You made ${} with a bonus of ${} as a {}".format(pay, bonus, job))
                                workedUsers.append(username)
                        else:
                            ultis.chat(s, "You have to have a job to work!")
                    else: 
                        ultis.chat(s, "No data found for you")
                    canCommand = True
                elif message.strip() == "!inv":
                    canCommand = False
                    if market.checkData(username):
                        inv = market.getInv(username)
                        ultis.chat(s, "Here is your inv: ")
                        for item in inv:
                            ultis.chat(s, "You have {} {}(s)".format(inv[item],item))
                    else:
                        ultis.chat(s, "You must have a profile")
                    canCommand = True
                elif message.strip() == "!lurk":
                    ultis.chat(s, "{} is now lurking".format(username))
                elif "!steal" in message:
                    target = jobFormat(message, "!steal ")
                    if market.checkData(target) and market.checkData(username):
                        chance = random.randint(1, 100)
                        if chance > 70:
                            market.changeMoney(target, ( -1 * chance))
                            market.changeMoney(username, chance)
                            ultis.chat(s, "Woah, you did it, you just walked away with ${} from {}".format(chance, target))
                        else:
                            ultis.chat(s, "Lol you failed and lost ${} If you're gonna try and rob someone, you better not get caught! This time though, you GOT caught! For that, you are going away for 30 looooong years. (30 Twitch Years is just 30 seconds in IRL time). Enjoy your time in the Bucket. Kappa".format(chance))
                            ultis.timeout(s, username, 30)
                            market.changeMoney(username,-1 * chance)
                    else:
                        ultis.chat(s, "Can't steal from them or you don't have a profile")

            if message.strip() == "m!r":
                    if username == "alphazulu22" or username ==  "backtosnack":
                        canCommand = True
                        mineCont = 0
                        workedUsers[:] = []
                        ultis.chat(s, "Reset cooldowns")
                        print("Reset cooldowns")
                    else:
                        ultis.chat(s, "Not owner")
                        print(username)
            if "m!c" in message:
                print(username)
                if username == "alphazulu22" or username == "backtosnack":
                    stuff = []
                    splitM = str(message).split()
                    for thing in splitM:
                        stuff.append(thing)
                    market.changeMoney(stuff[1], int(stuff[2]))
                    ultis.chat(s, "Money changed.... I think")
                else:
                    ultis.chat(s, "You can't cheat! :P")

main()
