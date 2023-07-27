my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for item in my_list:
    if item == 3 or item == 4:
        del my_list[my_list.index(item)]
