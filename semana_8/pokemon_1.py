
# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.
import json


def read_pokemon():
    with open('Notion/pokemon.json', 'r') as file:
        pokemon = json.load(file)
    return pokemon

def add_pokemon(pokemon):
    with open('Notion/pokemon.json', 'w') as file:
        json.dump(pokemon, file, indent = 4)
        
def main():
    pokemon = read_pokemon()
    
    name = input('Enter the pokemon name: ')
    type = input('Enter the type: ')
    hp = int(input('Enter the HP: '))
    attack = int(input('Enter the attack: '))
    defense = int(input('Enter the defense: '))
    sp_attack = int(input('Enter the Sp.Attack: '))
    sp_defense = int(input('Enter the Sp.Defense: '))
    speed = int(input('Enter the speed: '))
    
    new_pokemon = {
        "name": {
            "english": name
        },
        "type": [
            type
        ],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }
    
    pokemon.append(new_pokemon)
    add_pokemon(pokemon)
    

if __name__ == '__main__':
    main()
        