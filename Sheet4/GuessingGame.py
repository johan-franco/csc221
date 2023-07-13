from random import *
from gasp.utils import *
import getpass

def new_game():
    new_game = read_yesorno("Would you like to play again? ")
    if new_game == True:
        print("Choosing new number")
        randnum = randint(min_range, max_range)
        number_guesses = 0
    else:
        print("OK. Bye!")
        exit()
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

    
    return (x, y)

def twoplayer(s, pinfo):
    s = 0
    pname = input("Enter player 1's name: ")
    pname2 = input("Enter player 2's name: ")
    player1_guesser = 0
    player2_guesser = 0
    p1_games = 0
    p2_games = 0
    playerlist = [pname, pname2]
    pinfo = [[pname, player1_guesser, p1_games], [pname2, player2_guesser, p2_games]]
    entered_num = -1000000000
    while entered_num > max_range or entered_num < min_range:
        entered_num = int(getpass.getpass("%s enter your secret number:" %playerlist[s]))
        print(entered_num)
    s = 1 - s
    return s & pinfo & entered_num



wins = 0
total_games = 0
number_guesses = 0
ListNumberGuesses = []

min_range = read_number("What minimum range do you want to play the guessing game from? ")
max_range = read_number("What maximum range do you want to play the guessing game from? ")
limit_guesses = read_yesorno("""Would you like to limit the amount of guesses you can make?
Note that enabling this in second player will make winner be chosen by whoever is closest to number\n""")

if limit_guesses == True:
    limiter = read_number("What limit of guesses do you want? ")
else:
    limiter = -1

twoplay = read_yesorno("Would you like to play with 2 players (1v1)")

if twoplay == True:
    swap  = 0
    playerinfo = 0
    secret_num = 0
    twoplayer(swap, playerinfo, secret_num )
    guessernam= playerinfo[swap][0]
else:
    randnum = randint(min_range,max_range)

print("A number between %d and %d has been chosen." %(min_range, max_range))

while True:
    guess = read_number("Enter your guess: ")
    number_guesses += 1

    if guess == randnum or guess == secret_num:
        if twoplay == True:
            print("It took you %d guesses to guess %s's secret number, your total average guesses is %d" %(number_guesses, playerinfo[swap][0], ))
        else:
            ListNumberGuesses.append(number_guesses)
            total_games +=1
            wins +=1
            winrate = (wins/total_games)*100
            avguess = sum(ListNumberGuesses)/len(ListNumberGuesses)
            print("Congrats you guessed my number! \nIt took you %d guesses.\nIn total you have played %d times, your total average guesses to the correct answer is %d and your winrate is %d% " %(number_guesses, total_games,avguess, winrate ))
        new_game()
    elif number_guesses == limiter:
        total_games +=1
        print("You took %d guesses and went over the limiter!" %limiter)
        new_game()

    elif guess < randnum:
        print("My number is higher than %d" %guess)
    elif guess > randnum:
        print("Your number, %d, is higher than mine" %guess) 
    



