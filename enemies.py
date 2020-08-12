# -*- coding: utf-8 -*-

# basic commands for Player and Enemies
class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name
        
    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()
    
    def is_dead(self):
        return self.hp <= 0 
    
    def die(self):
        print( str(self.name) + " ist gestorben")

# Player Character
class player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp
        
    def die(self):
        exit("Du bist gestorben. Versuchs nochmal.")
        
    def rest(self):
        self.hp = self.max_hp
# Goblin enemie
class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")

# Ork enemie
class Ork(Character):
    def __init__(self):
        Character.__init__(self, 200, 20, "Ork")

liste = [Goblin(), Ork()]