def display_menu():
    print("1. SUM")
    print("2. SUBTRACTION")
    print("3. MULTIPLY")
    print("4. DIVISION")
    print("5. CANCEL")
    print("6. CLOSE")

def main():
    global_number = 0
    sum_number = 0
    sub_number = 0
    multiply_number = 0
    div_number = 0
    choice = 0
    option = True
    try:
        while option:
            display_menu()
            choice = int(input('Choose your option: '))
            match choice:
                case 1:
                    try:
                        sum_number = int(input('Enter the number to sum: '))
                        global_number += sum_number
                    except ValueError:
                        print('Enter a valid number!')
                    print(f'Result: {global_number}')
                case 2:
                    try:
                        sub_number = int(input('Enter the number to subtract: '))
                        global_number -= sub_number
                    except ValueError:
                        print('Enter a valid number!')
                    print(f'Result: {global_number}')
                case 3:
                    try:
                        multiply_number = int(input('Enter the number to multiply: '))
                        global_number *= multiply_number
                    except ValueError:
                        print('Enter a valid number!')
                    print(f'Result: {global_number}')
                case 4:
                    try:
                        div_number = int(input('Enter the number to divide: '))
                        global_number /= div_number
                    except ValueError:
                        print('Enter a valid number!')
                    print(f'Result: {global_number}')
                case 5:
                    global_number = 0
                    print(f'Result: {global_number}')
                case 6:
                    option = False
                    exit()
                case _:
                    exit()   
        print('Enter a valid option')
    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')

if __name__ == "__main__":
    main()  