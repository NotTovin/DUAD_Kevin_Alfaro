def bubble_sort(list_to_sort):
    
    for outer_index in range(0, len(list_to_sort) - 1):
        
        has_made_changes = False
        
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]

            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Elemento anterior: {previous_element}')

            if current_element < previous_element:
                
                print('El elemento actual es menor al anterior. Intercambiandolos...')
                
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = current_element
                
                has_made_changes = True

        if not has_made_changes:
            return


my_test_list = [8, 7, 6, 9, 5, 4, 3, 2, 1]
bubble_sort(my_test_list)

print(my_test_list)
