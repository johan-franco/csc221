from random import randint

right = 0

for i in range(10):
    ch10_num = randint(-10,10)
    ch10_num2 = randint(-10,10)

    answer = ch10_num * ch10_num2
    response = int(input("What is the value of %d and %d multiplied?" % (ch10_num,ch10_num2)))
    print("The answer is %d" %answer)

    if response == answer:
        right = right + 1
        print("Yes!")
    else:
        print("No!")


print("I asked you 10 questions you got %d right." %right)

if right == 10:
    print("Congrats on your perfect score")
elif right > 6:
    print("Good Job")
else:
    print("Maybe you should review your multiplication")
