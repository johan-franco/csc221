from random import *
from gasp.utils import *
import getpass

def twoplayer(h, s, pinfo, ent_num, mod):
    h = 1 - h
    s = 1 - s
    pname = input("Enter player 1's name: ")
    pname2 = input("Enter player 2's name: ")
    player1_guesser = 0
    player2_guesser = 0
    p1_games = 0
    p2_games = 0
    mod = 1
    playerlist = [pname, pname2]
    pinfo = [[pname, player1_guesser, p1_games], [pname2, player2_guesser, p2_games]]
    ent_num = -1000000000
    while ent_num > max_range or ent_num < min_range:
        ent_num = int(getpass.getpass("%s enter your secret number:" %playerlist[h]))
        print(ent_num)
    return h,s, pinfo, ent_num, mod

def new_game(randnum, number_guesses):
    new_game = read_yesorno("Would you like to play again? ")
    if new_game == True:
        print("Choosing new number")
        randnum = randint(min_range, max_range)
        number_guesses = 0
        return randnum & number_guesses
    else:
        print("OK. Bye!")
        exit()

def new_game2(ent_num, number_guesses, mod, s, pinfo, h):
    new_game = read_yesorno("Would you like to play again? ")
    print(mod)
    if new_game == True:
        number_guesses = 0
        h = 1 - h
        s = 1 - s
        ent_num = -10000
        while ent_num > max_range or ent_num < min_range:
            ent_num = int(getpass.getpass("%s enter your secret number: " % pinfo[s][0]))
            print(ent_num)
        return ent_num, number_guesses, s,h
    else:
        print("OK. Bye!")
        exit()

def against_comp(lmin, lmax):
    comp_guess = -1000
    range = lmax - lmin
    while True:
        new_min = lmin 
        new_max = lmax + range/100 # to let it guess the max num
        comp_num = 0
        ent_num  = int(getpass.getpass("Enter your secret number that you want the computer to search for: " ))
        while comp_guess != ent_num:
            middle = round((new_max - new_min)/2)
            comp_guess= new_min + middle
            comp_num += 1
            if comp_guess < ent_num:
                print("Computer's guess is %d, it was lower than your number." %(comp_guess))
                new_min = comp_guess
            elif comp_guess > ent_num:
                print("Computer's guess is %d, it was higher than your number" %(comp_guess))
                new_max = comp_guess

        print("Computer guessed %d, which is your number and it took %d tries." %(comp_guess,comp_num))
        again = read_yesorno("Play again against computer? ")
        if again == True:
            print("Starting...")
            continue
        else:
            print("Okay! Bye!")
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

computer = read_yesorno("Would you like to play with you hiding the number and the computer trying to find it?")
if computer == True:
    against_comp(min_range,max_range)

twoplay = read_yesorno("Would you like to play with 2 players (1v1)")

if twoplay == True:
    swap  = 0
    seeker = 1
    playerinfo = 0
    secret_num = 0
    mode = 0
    swap, seeker,playerinfo, secret_num, mode = twoplayer(swap, seeker, playerinfo, secret_num, mode)
    print(mode)
    hider_name= playerinfo[swap][0] + "'s"
else:
    mode = 0
    hider_name = 'My'
    secret_num = randint(min_range,max_range)

print("A number between %d and %d has been chosen." %(min_range, max_range))

while True:
    guess = read_number("%s,enter your guess: " %hider_name)
    number_guesses += 1

    if  guess == secret_num:
        if twoplay == True:
            playerinfo[seeker][1]= playerinfo[seeker][1] + number_guesses
            playerinfo[seeker][2] +=1
            cur_seeker_avg = playerinfo[seeker][1]/playerinfo[seeker][2]
            print("It took you %d guesses to guess %s's secret number, your total average guesses is %d" %(number_guesses, playerinfo[swap][0],cur_seeker_avg ))
            secret_num, number_guesses, swap, seeker = new_game2(secret_num ,number_guesses,mode, swap, playerinfo, seeker)
        else:
            ListNumberGuesses.append(number_guesses)
            total_games +=1
            wins +=1
            winrate = (wins/total_games)*100
            avguess = sum(ListNumberGuesses)/len(ListNumberGuesses)
            print("Congrats you guessed my number! \nIt took you %d guesses.\nIn total you have played %d times, your total average guesses to the correct answer is %d and your winrate is %d% " %(number_guesses, total_games,avguess, winrate ))
        
    elif number_guesses == limiter:
        total_games +=1
        print("You took %d guesses and went over the limiter!" %limiter)
        new_game(secret_num ,number_guesses,mode, swap, playerinfo)
    elif guess < secret_num:
        print("%s number is higher than %d" %(hider_name, guess))
    elif guess > secret_num:
        print("%s number, is lower than %d" %(hider_name,guess))
    



