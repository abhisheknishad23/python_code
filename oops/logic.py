class character:
    def __init__(self, name, health, attact, blodd):
        self.name = name
        self.health = health
        self.attack = attact
        self.blood = blodd

    def attack_enemy(self):
        print(f'{self.name} attack with power {self.attack} {self.blood}')

warrior = character('THOR',100, 60, 'red')
mage = character('gendal',80,50,'black')
archer = character('archer',80,40,'white')

warrior.attack_enemy()
mage.attack_enemy()
archer.attack_enemy()
