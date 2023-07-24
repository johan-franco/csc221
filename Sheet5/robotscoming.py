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
    robots = Robot()

    for i in range(numbots):
        pass
    robots.x = randint(0,63)
    robots.y = randint(0,47)
    robots.shape = Box((10 * robots.x, 10 * robots.y), 10, 10, filled=False, color=color.BLACK, thickness=1)

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

def move_robots():
    #Robot moves left & down
    if robots.x > player.x and robots.y > player.y:
        robots.x -= 1
        robots.y -= 1
        print("left & down")
    #Robot moves right & up
    elif robots.x < player.x and robots.y < player.y:
        robots.x += 1
        robots.y += 1
        print("right & up")
    #Robot moves left & up
    elif robots.x > player.x and robots.y < player.y:
        robots.x -= 1
        robots.y += 1
        print("left & up")
    #Robot moves right  & down
    elif robots.x < player.x and robots.y > player.y:
        robots.x += 1
        robots.y -= 1
        print("right & down")
    #Robot moves left
    elif robots.x > player.x and robots.y == player.y:
        robots.x -= 1
        print("left")
    #Robot moves right
    elif robots.x < player.x and robots.y == player.y:
        robots.x += 1
        print("right")
    #Robot moves down
    elif robots.y > player.y and robots.x == player.x:
        robots.y -= 1
        print("down")
    #Robot moves up
    elif robots.y < player.y and robots.x == player.x:
        robots.y += 1
        print("up")
    sleep(.5)
    move_to(robots.shape, (10 * robots.x, 10 * robots.y))
    return robots.x, robots.y

def check_collsions():
    if robots.y == player.y and robots.x == player.x:
        Text("You've been caught!", (320,240), color = color.RED, size = 40)
        sleep(3)
        return True
    
def collided():
    if robots.y == player.y and robots.x == player.x:
        return True

def safely_place(): 
    place_player()
    while collided():
        place_player()
    player.shape = Circle((10 * player.x + 5, 10 * player.y + 5), 5, filled=True)

begin_graphics()

place_robots()
safely_place()
numbots = 10
while True:
    player.x, player.y = move_player()
    robots.x, robots.y = move_robots()
    death = check_collsions()
    if death == True:
        break

end_graphics()




