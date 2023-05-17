#Tymoteusz Maj
#Github: Xeraoo
#Zadanie 10

import random

#Tworzymy klasę bazową GameEntity, która reprezentuje ogólną encję w grze, taką jak postać, obiekt, pojazd itp. 
#Zawiera ona podstawowe informacje o encji, takie jak nazwę i zdrowie.

class GameEntity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def __repr__(self):
        return f"{self.name} ({self.health}HP)"
    
    def __str__(self):
        return f"{self.name} ({self.health}HP)"
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} został pokonany!")
    
#Klasa Soldier dziedziczy po klasie GameEntity i reprezentuje żołnierza. 
# Dodatkowo, posiada ona parametr siły ataku (strength) oraz metodę attack, która wykonuje atak na wskazanego przeciwnika.

class Soldier(GameEntity):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength
    
    def attack(self, enemy):
        damage = random.randint(1, self.strength)
        print(f"{self.name} atakuje {enemy.name} i zadaje {damage} obrażeń!")
        enemy.take_damage(damage)
    
#Klasa Tank również dziedziczy po klasie GameEntity i reprezentuje czołg. 
# Ma ona dodatkowy parametr zbrojenia (armor) oraz metodę take_damage, która modyfikuje zadawane obrażenia 
# w zależności od poziomu opancerzenia. Posiada też metodę fire_main_gun, która wykonuje strzał z głównego działa.

class Tank(GameEntity):
    def __init__(self, name, health, armor):
        super().__init__(name, health)
        self.armor = armor
    
    def take_damage(self, amount):
        super().take_damage(amount // self.armor)
    
    def fire_main_gun(self, enemy):
        damage = random.randint(10, 20)
        print(f"{self.name} strzela z głównego działa i zadaje {damage} obrażeń!")
        enemy.take_damage(damage)
    
#Klasa Jet również dziedziczy po klasie GameEntity i reprezentuje samolot. Dodatkowo, posiada ona parametr prędkości (speed) 
# oraz metody attack i retreat, które odpowiednio wykonują nalot na przeciwnika lub ucieczkę na bezpieczną odległość.

class Jet(GameEntity):
    def __init__(self, name, health, speed):
        super().__init__(name, health)
        self.speed = speed
    
    def attack(self, enemy):
        damage = random.randint(5, 10)
        print(f"{self.name} wykonuje nalot i zadaje {damage} obrażeń!")
        enemy.take_damage(damage)
    
    def retreat(self):
        print(f"{self.name} wykonuje skok i ucieka na bezpieczną odległość!")
    
# Tworzenie instancji naszego wojska

soldier1 = Soldier("Gracz 1", 100, 20)
soldier2 = Soldier("Gracz 2", 100, 20)
tank1 = Tank("Czołg 1", 200, 5)
tank2 = Tank("Czołg 2", 200, 5)
jet1 = Jet("Samolot 1", 50, 10)
jet2 = Jet("Samolot 2", 50, 10)

# Symulacja Gry
print("START GRY!")
print(soldier1)
print(soldier2)
print(tank1)
print(tank2)
print(jet1)
print(jet2)
print()

# Faza 1: atak z powietrza
print("FAZA 1: atak z powietrza")
jet1.attack(tank1)
jet2.attack(tank1)
jet1.retreat()
jet2.retreat()
print()

# Faza 2: walka naziemna
print("FAZA 2: walka naziemna")
soldier1.attack(tank2)
soldier2.attack(tank2)
tank2.fire_main_gun(soldier1)
tank2.fire_main_gun(soldier2)
print()

print("KONIEC GRY!")
print(soldier1)
print(soldier2)
print(tank1)
print(tank2)
print(jet1)
