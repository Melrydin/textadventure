# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:19:49 2020

@author: Clemens
"""
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
        
class player(Character):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        self.max_hp = hp
        
    def die(self):
        exit("Du bist gestorben. Versuchs nochmal.")
        
    def rest(self):
        self.hp = self.max_hp

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")

class Ork(Character):
    def __init__(self):
        Character.__init__(self, 200, 20, "Ork")

liste = [Goblin(), Ork()]