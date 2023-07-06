from random import *
import time
import sqlite3

right = 0

quiztaker = input("Enter Name: ")
mode = input("Normal mode? (y/n) ")

if mode == 'y':
    for i in range(10):
        ch5_num = randint(-10,10)
        ch5_num2 = randint(-10,10)

        answer = ch5_num * ch5_num2
        response = int(input("What is the value of %d and %d multiplied? " % (ch5_num,ch5_num2)))
        print("The answer is %d" %answer)

        if response == answer:
            right = right + 1
            print("Yes! You are correct.")
        else:
            print("No, you are incorrect.")


    print("I asked you 10 questions you got %d right." %right)

    if right == 10:
        print("Congrats on your perfect score, %s." %quiztaker)
    elif right > 6:
        print("Good Job, %s." %quiztaker)
    else:
        print("%s, maybe you should review your multiplication." %quiztaker)
else:
    records = sqlite3.connect("highscores.db")
    cursor = records.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scores (name TEXT, record INTEGER)")

    ready = input("Are you ready for Time Attack? (y/n)")
    if ready == 'y':
        print("Good Luck! ... ")
    else:
        print("Starting anyway ... ")
    
    start_time = time.time()
    duration = 10
    score = 0

    while True:
         current_time = time.time()
         elapsed_time = (current_time - start_time)

         ta_num = randint(-10,10)
         ta_num2 = randint(-10,10)

         answer = ta_num * ta_num2
         response = int(input("What is the value of %d and %d multiplied? " % (ta_num,ta_num2))) 

         if response == answer:
            score = score + 1
         else:
            continue

         if elapsed_time == 5:
             print("5 seconds left")
         elif elapsed_time > 10:
             print("Time Attack has concluded, you scored %d" %score)
             break
         else:
             continue
    print("Saving/Updating %s's score" %quiztaker)
    try:
        cursor.execute("INSERT INTO scores VALUES (?, ?)", (quiztaker,score))
    except:
        cursor.execute("UPDATE scores VALUES (?, ?)",(quiztaker, score))
    records.commit()
    print(cursor.fetchall())
    cursor.close()