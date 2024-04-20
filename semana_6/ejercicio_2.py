# def variable_local():
#     v_local = 'Hola soy una variable local'
#     print(v_local)

# print(v_local)

v_global = 'Hola Mundo soy una variable global'

def variable_global():
    v_global = 'Estoy dentro de una funcion'
    print(v_global)

variable_global()
print(v_global)