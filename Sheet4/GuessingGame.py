from random import *

i = 0
randnum = randint(1,1000)

print("A number between 1 and 1000 has been chosen.")
while True:
    try:
        guess = int(input("Enter your guess: "))
    except:
        print("That's not a number! Try again!")
        continue

    if guess == randnum:
        print("Congrats you guessed my number! \nIt took you %d guesses" %i)
        break
    elif guess < randnum:
        print("My number is higher than %d" %guess)
    elif guess > randnum:
        print("Your number, %d, is higher than mine" %guess) 
    i += 1
    
    if i == 4:
        new_game = input("You took four guesses would you like to play again? (y/n)\n")
    
    if new_game == 'y':
        print("Choosing new number")
        randnum = randint(1, 1000)
        i = 0
        continue
    else:
        print("OK. Bye!")
        break



