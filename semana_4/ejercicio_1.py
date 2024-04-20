#String + String
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# nombre_completo = nombre + apellido
# print(nombre_completo)

#String + Integer

# File "g:\Programacion\Sintaxis_1", line 10, in <module>
#     nombre_edad = nombre + edad
#                   ~~~~~~~^~~~~~
# TypeError: can only concatenate str (not "int") to str

# nombre = input("Ingrese su nombre: ")
# edad = int(input('Ingrese su edad: '))
# nombre_edad = nombre + edad
# print(nombre_edad)

#Integer + String

#  File "g:\Programacion\Sintaxis_1", line 22, in <module>
#     nombre_edad = edad + nombre
#                   ~~~~~^~~~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# nombre = input("Ingrese su nombre: ")
# edad = int(input('Ingrese su edad: '))
# nombre_edad = edad + nombre
# print(nombre_edad)

#list + list
# lista1 = [11,21,31,41]
# lista2 = [10,20,30,40]
# suma_lista = lista1 + lista2
# print(suma_lista)

#String + List
# Traceback (most recent call last):
#   File "g:\Programacion\Sintaxis_1", line 28, in <module>
#     lista_nombre = nombre + lista1
#                    ~~~~~~~^~~~~~~~
# TypeError: can only concatenate str (not "list") to str
# PS G:\Programacion> 

# lista1 = [11,21,31,41]
# nombre = 'Kevin'
# lista_nombre = nombre + lista1
# print(lista_nombre)

#float + int
# edad = int(input('Ingrese su edad: '))
# decimales = float(input('Ingrese su edad: '))
# sumatoria = decimales + edad
# print(sumatoria)

#bool + bool
bool1 = False
bool2 = False
sumatoria = bool1 + bool2
print(sumatoria)