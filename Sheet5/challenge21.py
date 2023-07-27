my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(my_list)):
    if my_list[i] == 3 or my_list[i] == 7:
        del my_list[i]

        i = i - 1
    print(i)