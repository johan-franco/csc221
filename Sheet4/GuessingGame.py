from random import *
from gasp.utils import *

number_guesses = 0
ListNumberGuesses = []

min_range = read_number("What minimum range do you want to play the guessing game from? ")
max_range = read_number("What maximum range do you want to play the guessing game from? ")
limit_guesses = read_yesorno("""Would you like to limit the amount of guesses you can make? \n
Note that enabling this in second player will make winner be chosen by whoever is closest to number\n""")

if limit_guesses == True:
    limiter = read_number("What limit of guesses do you want? ")

randnum = randint(min_range,max_range)

print("A number between %d and %d has been chosen." %(min_range, max_range))

while True:
    guess = read_number("Enter your guess: ")

    if guess == randnum or number_guesses == limiter:
        if guess == randnum:
            ListNumberGuesses.append(number_guesses)
            print("Congrats you guessed my number! \nIt took you %d guesses." %number_guesses)

        else:
            new_game = input("You took four guesses would you like to play again? (y/n)\n")
        break
    elif guess < randnum:
        print("My number is higher than %d" %guess)
    elif guess > randnum:
        print("Your number, %d, is higher than mine" %guess) 
    number_guesses += 1
    
    if number_guesses == limiter:
        new_game = input("You took four guesses would you like to play again? (y/n)\n")
    
        if new_game == 'y':
            print("Choosing new number")
            randnum = randint(1, 1000)
            number_guesses = 0
            continue
        else:
            print("OK. Bye!")
            break



