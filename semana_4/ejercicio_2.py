nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))

if(edad < 5 ):
    clasificacion = 'bebe'
    print(f'{nombre} {apellido} {edad} {clasificacion}')
elif(edad < 11):
    clasificacion = 'niño'
    print(f'{nombre} {apellido} {edad} {clasificacion}')
elif(edad < 14):
    clasificacion = 'preadolescente'
    print(f'{nombre} {apellido} {edad} {clasificacion}')
elif(edad < 18):
    clasificacion = 'adolescente'
    print(f'{nombre} {apellido} {edad} {clasificacion}')
elif(edad < 26):
    clasificacion = 'adulto joven'
    print(f'{nombre} {apellido} {edad} {clasificacion}')
elif(edad < 59):
    clasificacion = 'adulto'
    print(f'{nombre} {apellido} {edad} {clasificacion}')
elif(edad >= 59):
    clasificacion = 'adulto mayor'
    print(f'{nombre} {apellido} {edad} {clasificacion}')



