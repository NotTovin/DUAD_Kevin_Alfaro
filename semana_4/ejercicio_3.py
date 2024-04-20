numero_secreto = 3
numero = int(input('Ingrese un numero del 1 al 10: '))

while(numero != numero_secreto):
	print('Numero incorrecto')
	numero = int(input('Ingrese un numero del 1 al 10: '))

print('Adivinaste el numero secreto')
print(f'El numero secreto era: {numero_secreto}')