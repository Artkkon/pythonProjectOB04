from abc import ABC, abstractmethod
from random import choice

class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f'{self.name} выбрал {weapon}')

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, fighter):
        fighter.health -= self.damage

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self, monster):
        print("Атака мечом")
        monster.health -= 2

class Bow(Weapon):
    def attack(self, monster):
        print("Атака луком")
        monster.health -= 1


fighter = Fighter("Вася", 15)
monster = Monster("Монстр", 10, 2)
sword = Sword()
bow = Bow()

while fighter.health > 0 and monster.health > 0:
    fighter.change_weapon(choice([sword, bow]))
    fighter.weapon.attack(monster)
    monster.attack(fighter)
    print(f"Здоровье {fighter.name}: {fighter.health}")
    print(f"Здоровье {monster.name}: {monster.health}")

if fighter.health > 0:
    print(f"{fighter.name} победил!")
else:
    print(f"{monster.name} победил!")
