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
    return job.lower()

def main():
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
            message = CHAT_MSG.sub("", response)
            print(response)

         #Custom Commands 0w0 
            if canCommand:
                #print(len(str(message)))
                #I should probably actaully do this command correctly, nahhhh
                if message.strip() == "!time":
                    #I really don't want to type a time command
                    ultis.chat(s, "I don't know, you're the one on the computer, I'm just a program")
                #about, aka me flexing I wrote this
                elif message.strip() == "!about":
                    #sends the about
                    ultis.chat(s, cfg.about)
                elif message.strip() == "!toby":
                    ultis.chat(s, toby)
                elif message.strip() == "m!reset":
                    if username == "alphazulu22":
                        mineCont = 0
                        workedUsers[:] = []
                        ultis.chat(s, "Reset cooldowns")
                    else:
                        ultis.chat(s, "Not owner")
                #Question Command
                elif message.strip() == "!question":
                    #sends a question 
                    question = qst[random.randint(0, len(qst)- 1)] #Math is fun
                    ultis.chat(s, question)
                #Nice
                elif "69" in message:
                    ultis.chat(s, "Nice")
                elif "who is joe?" in message.lower():
                    ultis.chat(s, "Joe Mama")
                #Roll a d6 command
                elif message.strip() == "!d6":
                    diceRoll = random.randint(1, 6)
                    ultis.chat(s, diceRoll)
                elif message.strip() == "!POG":
                    ultis.chat(s, pog)
                #Gun Command
                elif message.strip() == "!shoot":
                    #Bang Bang Bang
                    gunMessage = "{} shoot a dummy with a{} and did {} points of damage".format(username, guns[random.randint(0, len(guns)- 1)],random.randint(0, 100))
                    ultis.chat(s, gunMessage)
                elif message.strip() == "!chance":
                    winChance = random.randrange(1, 101)
                    if username == "alphazulu22":
                        ultis.chat(s, "Sorry Alpha, no cuts for the programmer, but the win rate is {}%".format(winChance))
                    else:
                        ultis.chat(s, "The chance of the next fight starter winning is {}%".format(winChance))
                elif "!fight" in message and len(str(message)) <= 60:
                    if winChance == 0:
                        ultis.attack(s, username, message, 50)
                        print("Fair Match")
                    else:
                        ultis.attack(s, username, message, winChance)
                        winChance = 0
                elif "!battle" in message and len(str(message)) <= 10:
                    ultis.chat(s, "AlphaZulu22 has won and has slayed any challenger that dares to question this massive victory. He has delt 999,999,999 damage and healed for double that. He has a base life gen of 100,000 per nano sec and has a base health higher than infinity. He can not be slayed.")
                #   Cool economy Commands

                elif message.strip() == "!profile":
                    if market.checkData(username):
                        data = market.profile(username)
                        ultis.chat(s, username + ": ")
                        ultis.chat(s, " level: " + str(data[1]))
                        ultis.chat(s, " cash: $" + str(data[2]))
                        ultis.chat(s, " job: "  + str(data[3]))
                    else:
                        market.makeData(username)
                        ultis.chat(s, "No data was found, so a profile was made")
                elif message.strip() == "!bal":
                    if market.checkData(username):
                        data = market.profile(username)
                        ultis.chat(s, username + " has a balance of $" +  str(data[2]))
                    else:
                        market.makeData(username)
                        ultis.chat(s, "No data was found, so a profile was made")
                elif message.strip() == "!mine":
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
                elif "!getjob" in message and len(str(message)) <= 23:
                    job = jobFormat(message, "!getjob ")
                    jobCheck = market.getJob(username, job)
                    if jobCheck and market.checkData(username):
                        ultis.chat(s, "Congrats you now have a job as a {}".format(job))
                    else:
                        ultis.chat(s, "Not a valid job or you have yet to set up your profile")
                elif message.strip() == "!joblist":
                    send = str(market.jobList.keys()).replace("'", "").replace("[", "").replace("]", "")
                    ultis.chat(s, "The jobs you can have are: " + send)
                elif "!salary" in message and len(str(message)) <= 23:
                    job = jobFormat(message, "!salary ")
                    if market.jobList.has_key(job):
                        salary = market.jobList[job]
                        ultis.chat(s, "The base salary of a {} is ${}, with a maxium bonus of ${}".format(job, salary[0], salary[2]))
                    else:
                        ultis.chat(s, "Not a valid job")
                elif message.strip() == "!work":
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
                elif "!shop" in message and len(str(message)) <= 30:
                    print()


main()
