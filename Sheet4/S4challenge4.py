#A break will only take you out one loop at a time

while True:
    while True:
        x =input("Enter Number: ")
        if x == '10':
            break

    print("Left first while loop")
print("Exited all while loops") 