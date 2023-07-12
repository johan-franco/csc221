from random import *
from gasp.utils import *

def adjust_settings(x,y):
    changer = read_yesorno("Would you like to change any settings? ")
    if changer == True :
        pass
    else:
        return
    change_limit= read_yesorno("Change limiter? ")
    if change_limit == True:
        x = read_number("What minimum range do you want to play the guessing game from? ")
        y = read_number("What maximum range do you want to play the guessing game from? ")
        
    change_player = read_yesorno("Would you like to change the amount of players?")
    if change_player == True:
        p = read_number("How many players do you want to change it to?")
    

    x = read_number("What minimum range do you want to play the guessing game from? ")
    y = read_number("What maximum range do you want to play the guessing game from? ")
    return (x, y)

number_guesses = 0
ListNumberGuesses = []
min_range = read_number("What minimum range do you want to play the guessing game from? ")
max_range = read_number("What maximum range do you want to play the guessing game from? ")
limit_guesses = read_yesorno("""Would you like to limit the amount of guesses you can make?
Note that enabling this in second player will make winner be chosen by whoever is closest to number\n""")

if limit_guesses == True:
    limiter = read_number("What limit of guesses do you want? ")
else:
    limiter = 0

randnum = randint(min_range,max_range)

print("A number between %d and %d has been chosen." %(min_range, max_range))

while True:
    guess = read_number("Enter your guess: ")
    number_guesses += 1

    if guess == randnum or number_guesses == limiter:
        if guess == randnum:
            ListNumberGuesses.append(number_guesses)
            print("Congrats you guessed my number! \nIt took you %d guesses." %number_guesses)
        else:
            print("You took %d guesses and went over the limiter!" %limiter)
        new_game = read_yesorno("Would you like to play again? ")
        if new_game == True:
            print("Choosing new number")
            randnum = randint(min_range, max_range)
            number_guesses = 0
        else:
            print("OK. Bye!")
            break


    elif guess < randnum:
        print("My number is higher than %d" %guess)
    elif guess > randnum:
        print("Your number, %d, is higher than mine" %guess) 
    



