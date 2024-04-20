my_list = [4, 3, 6, 1, 7, 8, 5, 3, 10]

if len(my_list) < len(my_list):
    print(my_list)
else:
    primer_elemento = my_list[0]
    ultimo_elemento = my_list[-1]
    my_list[0] = ultimo_elemento
    my_list[-1] = primer_elemento
    print(my_list)
    
