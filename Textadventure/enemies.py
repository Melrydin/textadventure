# -*- coding: utf-8 -*-

# basic commands for Player and Enemies
class Character:
    def __init__(self, name, hp, attack):
        self.hp = hp
        self.attack = attack
        self.name = name
        
    def get_hit(self, attack):
        self.hp = self.hp - attack
        if self.hp <= 0:
            self.die()
    
    def is_dead(self):
        return self.hp <= 0 
    
    def die(self):
        print( str(self.name) + " ist gestorben")

# Player Character
class player(Character):
    def __init__(self, name, hp, attack, mana, endurance):
        Character.__init__(self, name, hp, attack)
        self.max_hp = hp
        self.mana = mana
        self.endurance = endurance
        
    def die(self):
        exit("Du bist gestorben. Versuchs nochmal.")
        
    def rest(self):
        if self.hp < self.max_hp:
            self.hp = self.hp + (self.max_hp * 0.1)
            if self.hp > self.max_hp:
                self.hp = self.max_hp

# Goblin enemie
class Goblin(Character):
    def __init__(self):
        Character.__init__(self, "Goblin", 100, 10)

# Ork enemie
class Ork(Character):
    def __init__(self):
        Character.__init__(self, "Ork", 200, 20)

enemie_list = [Goblin(), Ork()]