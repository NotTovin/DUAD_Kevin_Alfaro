1. Cree una clase de `Circle` con:
    1. Un atributo de `radius` (radio).
    2. Un método de `get_area` que retorne su área.
2. Cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    3. Un método para bajar pasajeros uno por uno (en cualquier orden).
3. Modifique el proyecto  para usar objetos (creando una clase de `Student`) para guardar la información de los estudiantes.
    1. Hay que cambiar los estudiantes de diccionarios a objetos.
    2. Hay que convertir la data del csv de diccionario a objeto al importar.
    3. Hay que convertir los objetos a diccionario al exportar a csv.
    4. Hay que modificar el acceso a los keys para accesar a atributos.
        1. student[’Name’] → student.name
4. Cree las siguientes clases:
    1. `Head`
    2. `Torso`
    3. `Arm`
    4. `Hand`
    5. `Leg`
    6. `Feet`
    7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.
        1. Por ejemplo (*este código esta incompleto, pero describe la idea*):
            
            ```python
            class Torso:
            	def __init__(self, head, right_arm, ...):
            		self.head = head
            		self.right_arm = right_arm
            		...
            
            class Arm:
            	def __init__(self, hand):
            		self.hand = hand
            
            right_hand = Hand()
            right_arm = Arm(right_hand)
            torso = (head, right_arm)
            ```