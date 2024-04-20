my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in my_list:
    record =  index % 2
    if record != 0:
        my_list.remove(index)

print(my_list)
