from gasp import *
from pygame import *
from random import *
from gasp.utils import *

def place_player( ):
    global player_shape , px, py
    px = randint(0,63)
    py = randint(0,47)

    player_shape = Circle((10 * px + 5, 10 * py + 5), 5, filled=True)

    print("Here I am!")

def place_robot():
    global rx,ry, roboshape
    rx = randint(0,63)
    ry = randint(0,47)
    roboshape = Box()

def move_player():
    direction =  read_number(update_when('key_pressed'))
    
        
    if direction == '1':
        px -= 1
        py += 1
    elif direction == '2':
        py += 1
    elif direction == '3':
        px += 1
        py += 1
    elif direction == '4':
        px -= 1
    elif direction == '5':
        pass
    elif direction == '6':
        px += 1
    elif direction == '7':
        px -= 1
        py -= 1
    elif direction == '8':
        py -= 1
    elif direction == '9':
        px += 1
        py -= 1

    move_to(player_shape, (10 * px + 5, 10 * py + 5))

begin_graphics()

finished = False

place_player()

while not finished:
    move_player()

end_graphics()




