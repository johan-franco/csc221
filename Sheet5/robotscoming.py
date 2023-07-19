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
    roboshape = Box((10 * rx, 10 * ry), 10, 10, filled=False, color=color.BLACK, thickness=1)

def move_player():
    direction =  read_number(update_when('key_pressed'))
    
    #move up & left
    if direction == '1':
        px -= 1
        py += 1
    #move up
    elif direction == '2':
        py += 1
    #move up & right
    elif direction == '3':
        px += 1
        py += 1
    #move left
    elif direction == '4':
        px -= 1
    #stay still
    elif direction == '5':
        pass
    #move right
    elif direction == '6':
        px += 1
    #move left & down
    elif direction == '7':
        px -= 1
        py -= 1
    #move down
    elif direction == '8':
        py -= 1
    #move right & down
    elif direction == '9':
        px += 1
        py -= 1

    move_to(player_shape, (10 * px + 5, 10 * py + 5))

def move_robot():
    #Robot moves left & down
    if rx > px & ry > py:
        rx -= 1
        ry -= 1
    #Robot moves right & up
    elif rx < px & ry < py:
        rx += 1
        ry += 1
    #Robot moves left & up
    elif rx > px & ry < py:
        rx -= 1
        ry += 1
    #Robot moves right  & down
    elif rx < px & ry > py:
        rx += 1
        ry -= 1
    #Robot moves left
    elif rx > px & ry == py:
        rx -= 1
    #Robot moves right
    elif rx < px & ry == py:
        rx += 1
    #Robot moves down
    elif ry > py & rx == px:
        ry -= 1
    #Robot moves up
    elif ry < py & rx == px:
        ry += 1
    sleep(1)
    move_to(roboshape, (10 * px, 10 * py))
    sleep(10)

def check_collsions():
    if ry == py & rx == px:
        pass


begin_graphics()

finished = False

place_player()
place_robot()
move_player()
move_robot()

while not finished:
    move_player()

end_graphics()




