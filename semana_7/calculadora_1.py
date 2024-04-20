def display_menu():
    print("1. SUM")
    print("2. SUBTRACTION")
    print("3. MULTIPLY")
    print("4. DIVISION")
    print("5. CANCEL")
    print("6. CLOSE")

def sum(global_number, sum_number):
    try:
        global_number += sum_number
        print(f'{global_number}')
    except ValueError as ex:
        print(f'Enter a valid number')
        raise ex
    return global_number

def subtraction(global_number, sub_number):
    try:
        global_number -= sub_number
        print(f'{global_number}')
    except ValueError as ex:
        print('Enter a valid number')
        raise ex
    return global_number

def multiply(global_number, multiply_number):
    try:
        global_number *= multiply_number
        print(f'{global_number}')
    except ValueError as ex :
        print('Enter a valid number')
        raise ex
    return global_number

def division(global_number, div_number):
    try:
        global_number /= div_number
        print(f'{global_number}')
    except (ValueError, ZeroDivisionError) as ex:
        print('Enter a valid number')
        raise ex
    return global_number

def cancel(global_number):
    try:
        global_number = 0
        print(f'{global_number}')
    except ValueError as ex: 
        print('Enter a valid number')
        raise ex
    return global_number

def close():
    exit()


def main():
    global_number = 0
    sum_number = 0
    sub_number = 0
    multiply_number = 0
    div_number = 0
    option = True
    try:
        display_menu()
        while option:
            choice = input('Choose your option: ')
            if choice == '1':
                try:
                    sum_number = int(input('Enter the number to sum: '))
                    global_number = sum(global_number, sum_number)
                except ValueError:
                    print('Please enter a valid number!')
            elif choice == '2':
                try:
                    sub_number = int(input('Enter the number to subtract: '))
                    global_number = subtraction(global_number, sub_number)
                except ValueError:
                    print('Please enter a valid number!')
            elif choice == '3':
                try:
                    multiply_number = int(input('Enter the number to multiply: '))
                    global_number = multiply(global_number, multiply_number)
                except ValueError:
                    print('Please enter a valid number!')
            elif choice == '4':
                try:
                    div_number = int(input('Enter the number to divide: '))
                    global_number = division(global_number, div_number)
                except ValueError:
                    print('Please enter a valid number!')
            elif choice == '5':
                global_number = cancel(global_number)
            elif choice == '6':
                option = False
                close()  
            else:
                print('Invalid option')
        
    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')

if __name__ == "__main__":
    main()  
