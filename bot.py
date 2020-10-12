import cfg
import ultis

import random
import socket
import re 
import time
from time import sleep

ms = cfg.messageSend
qst = cfg.questions
guns = cfg.guns
x = 0
y = 0
winChance = 0
pog = "backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG backto10SnackPOG backto10SnackGoldPOG"
toby = "backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby backto10SnackToby"



def main():
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
            elif "!fight" in message:
                if winChance == 0:
                    ultis.attack(s, username, message, 50)
                    print("Fair Match")
                else:
                    ultis.attack(s, username, message, winChance)
                    winChance = 0
            elif "!battle" in message:
                ultis.chat(s, "AlphaZulu22 has won and has slayed any challenger that dares to question this massive victory. He has delt 999,999,999 damage and healed for double that. He has a base life gen of 100,000 per nano sec and has a base health higher than infinity. He can not be slayed.")
main()
