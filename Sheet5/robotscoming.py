from gasp import *
from random import *
from gasp.utils import *

class Player:
    pass

class Robot:
    pass


def place_player( ):
    global player
    player = Player()
    player.x = randint(0,63)
    player.y = randint(0,47)

    print("Here I am!")

def place_robots():
    global robots
    global roblist
    roblist = []
    while len(roblist) < numbots:
        robots = Robot()
        robots.x = randint(0,63)
        robots.y = randint(0,47)
        if not collided(robots, roblist):
            robots.shape = Box((10 * robots.x, 10 * robots.y), 10, 10, filled=False, color=color.BLACK, thickness=1)
            roblist.append(robots)
    

def move_player():
    direction =  (update_when('key_pressed'))
    
    #move up & left
    while direction == '5':
        remove_from_screen(player.shape)
        safely_place()
        direction = update_when('key_pressed')

    if direction == '1':
        player.x -= 1
        player.y += 1
    #move up
    elif direction == '2':
        player.y += 1
    #move up & right
    elif direction == '3':
        player.x += 1
        player.y += 1
    #move left
    elif direction == '4':
        player.x -= 1
    #move right
    elif direction == '6':
        player.x += 1
    #move left & down
    elif direction == '7':
        player.x -= 1
        player.y -= 1
    #move down
    elif direction == '8':
        player.y -= 1
    #move right & down
    elif direction == '9':
        player.x += 1
        player.y -= 1
    sleep(.5)
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))
    return player.x, player.y

def move_robots(list_of_bots):
    for bot in list_of_bots:
        botCount = 0 
        #Robot moves left & down
        if bot.x > player.x and bot.y > player.y:
            bot.x -= 1
            bot.y -= 1
            print("left & down")
        #Robot moves right & up
        elif bot.x < player.x and bot.y < player.y:
            bot.x += 1
            bot.y += 1
            print("right & up")
        #Robot moves left & up
        elif bot.x > player.x and bot.y < player.y:
            bot.x -= 1
            bot.y += 1
            print("left & up")
        #Robot moves right  & down
        elif bot.x < player.x and bot.y > player.y:
            bot.x += 1
            bot.y -= 1
            print("right & down")
        #Robot moves left
        elif bot.x > player.x and bot.y == player.y:
            bot.x -= 1
            print("left") 
        #Robot moves right
        elif bot.x < player.x and bot.y == player.y:
            bot.x += 1
            print("right")
        #Robot moves down
        elif bot.y > player.y and bot.x == player.x:
            bot.y -= 1
            print("down")
        #Robot moves up
        elif bot.y < player.y and bot.x == player.x:
            bot.y += 1
            print("up")
        sleep(.15)
        move_to(bot.shape, (10 * bot.x, 10 * bot.y))
        list_of_bots[botCount] = bot
        botCount += 1
    return list_of_bots

def check_collsions():
    if robots.y == player.y and robots.x == player.x:
        Text("You've been caught!", (320,240), color = color.RED, size = 40)
        sleep(3)
        return True
    
def collided(object, list_of_bots):
    for item in list_of_bots:
        if object.x == item.x and object.y == item.y:
            return True
    return False

def safely_place(): 
    while True:
        place_player()
        if not collided(player, roblist):
            break
    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

def robot_crashed(the_bot):
    for a_bot in robots:
        if a_bot.x == the_bot.x and a_bot.y == the_bot.y and the_bot.x != a_bot.x and the_bot.y != a_bot.y:  
            return a_bot
    return False
    
begin_graphics()
numbots = 10
place_robots()
safely_place()
while True:
    player.x, player.y = move_player()
    roblist = move_robots(roblist)
    death = check_collsions()
    if death == True:
        break

end_graphics()




