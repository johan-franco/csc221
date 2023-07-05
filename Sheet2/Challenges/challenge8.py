from random import randint

ch8_num = randint(1,10)
ch8_num2 = randint(1,10)

answer = ch8_num * ch8_num2
response = int(input("What is the value of %d and %d multiplied?" % (ch8_num,ch8_num2)))
print("The answer is %d" %answer)

if response == answer:
    print("Yes!")
else:
    print("No!")
