class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health =  health
    
    def attack(self):
        print(f'{self.name} attacks!')
    
    def receive_damage(self, damage):
        self.health -= damage
        print(f"{self.name} receives {damage} damage! Health is now {self.health}.")
        

class GhostMoves:
    def shadow_claw(self):
        print(f'{self.name} used Shadow Claw')

class PoisonMoves:
    def sludge_bomb(self):
        print(f'{self.name} used Sludge Bomb')

class GrassMoves:
    def bullet_seed(self):
        print(f'{self.name} used Bullet Seed')
        
class FairyMoves:
    def fairy_wind(self):
        print(f'{self.name} used Fairy Wind')

class GhostPoisonPokemon(Pokemon, GhostMoves, PoisonMoves):
    
    def __init__(self, name, health):
        super().__init__(name, health)

class GrassPokemon(Pokemon, GrassMoves):
    def __init__(self, name, health):
        super().__init__(name, health)

gengar = GhostPoisonPokemon('Gengar', 150)
exeggutor = GrassPokemon('Exeggutor', 120)
gengar.attack()
gengar.shadow_claw()
exeggutor.receive_damage(50)
exeggutor.attack()
exeggutor.bullet_seed()
gengar.receive_damage(20)
gengar.sludge_bomb()
exeggutor.receive_damage(26)


