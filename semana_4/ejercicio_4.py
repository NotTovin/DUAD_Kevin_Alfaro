first_number = int(input('Ingrese el numero: '))
second_number = int(input('Ingrese el numero: '))
third_number = int(input('Ingrese el numero: '))

higher_number = first_number

if(second_number>higher_number):
    higher_number = second_number

if(third_number>higher_number):
    higher_number = third_number

print(f'El numero mayor es: {higher_number}')


