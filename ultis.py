#Utils.py
#Uiltiy functions

import cfg
import time
import random
from time import sleep

#Returns a fight message
def fightMess(first, sec):
    return str(first) + cfg.attacks[random.randint(0, len(cfg.attacks)- 1)] + str(sec)

#Sends a message to chat
def chat(sock, msg):
    #Sends chat to server
    print(msg)
    sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg))
def timeout(sock, user, seconds=60):
    chat(sock, ".timeout {} {}".format(user, seconds))


def winFight(sock, user,target):
    #Get's the loser from the message
    loser = target.replace("!fight", "")
    loser = loser.replace("\r","")
    loser = loser.replace("\n","")
    if loser == "":
        loser = "a bokoblin"
    chat(sock, fightMess(user, loser))
    time.sleep(3)
    chat(sock, fightMess(loser, user))
    time.sleep(3)
    chat(sock, fightMess(user, loser))
    time.sleep(3)
    chat(sock, "{} has won".format(user))
def loseFight(sock, user, target):
 #Gets the winner from the message 
    winner = target.replace("!fight", "")
    winner = winner.replace("\r","")
    winner = winner.replace("\n","")
    if winner == "":
        winner = "a bokoblin"
    chat(sock, fightMess(user, winner))
    time.sleep(3)
    chat(sock, fightMess(winner, user))
    time.sleep(3)
    chat(sock, fightMess(user, winner))
    time.sleep(3)
    chat(sock, fightMess(winner, user))
    time.sleep(3)
    lose = "{} lost to {}".format(user, winner)
    chat(sock, lose)
def attack(sock, user, target, high):
    x = random.randrange(1, 101)
    #Rigged
    #  if user == "alphazulu22":
    #      x = 10
    # If num is greater than percent, then the user who strated the 
    if x <= high:
        repate = random.randrange(1,3)
        if repate > 2:
            winFight(sock, user, target)
            winFight(sock, user, target)
        else:
            winFight(sock, user, target)
    else:
        repate = random.randrange(1,5)
        if repate > 4:
            loseFight(sock, user, target)
            loseFight(sock, user, target)
        else:
            loseFight(sock, user, target)


def checkInt(num):
    try: 
        int(num)
        return True
    except ValueError:
        print("num is not an int")
        return False