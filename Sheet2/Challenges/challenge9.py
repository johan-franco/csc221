from random import randint

for i in range(3): 
    win1 = randint(1, 10)
    win2 = randint(11, 20)
    win3 = randint(21, 30)

    winners = str(win1) + " " + str(win2) + " " + str(win3)

    print("And the three lucky winners are: " + winners + ".")
