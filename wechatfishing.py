from wxpy import *
import pysnooper
import random

bot = Bot(cache_path=True)



class reply:
    fish1 = "a.. sock? +0"
    fish2 = "a plankter... +1"
    fish3 = "a catfish. +3"
    fish4 = "a giant squid! +5"
    fish5 = "a MEGALODON!!! +10"
    welcome = "Welcome to the fishing game!"
    uc = "You caught"
    
class Turn:
    player1turn = True
    result = ""
    switch = False
class Points:
    p1 = 0
    p2 = 0

    
    

@bot.register()
def bot_listener(msg):
    if msg.text == "fish":
        msg.reply(reply.welcome)
        bot.registered.enable(play_game)
        bot.registered.disable(bot_listener)
        

@bot.register(enabled=False)
def play_game(msg):
    if Turn.switch == True:
        Turn.player1turn = not Turn.player1turn
        Turn.switch = False
    if "fish" in msg.text:
        if Turn.player1turn:
            msg.reply(f"Player 1's Turn, {Points.p1} points")
        else:
            msg.reply(f"Player 2's Turn, {Points.p2} points")
        msg.reply(fish())
    elif "stop" in msg.text:
        msg.reply("You ended your turn! It is the other player's turn.")
        Turn.switch = True
 

@pysnooper.snoop("./log.log",variables=('Turn.player1turn'))
def fish():    
    num = random.randint(1,6)
    
    if num == 1:
        return (reply.uc, reply.fish1)
    
    elif num == 2:
        if Turn.player1turn:
            Points.p1 += 1
        else:
            Points.p2 += 1
        return (reply.uc, reply.fish2)
        
    elif num == 3:
        if Turn.player1turn:
            Points.p1 += 3
        else:
            Points.p2 += 3
        return (reply.uc, reply.fish3)
    
    elif num == 4:
        if Turn.player1turn:
            Points.p1 += 5
        else:
            Points.p2 += 5
        return (reply.uc, reply.fish4)
    
    elif num == 5:
        if Turn.player1turn:
            Points.p1 += 10
        else:
            Points.p2 += 10
        return (reply.uc, reply.fish5)
    
    else:
        if Turn.player1turn:
            Points.p1 = 0
        else:
            Points.p2 = 0
        Turn.switch = True
        return (reply.uc, "an electric eel! You have zero points and your Turn is over.")
            
            
embed()
    