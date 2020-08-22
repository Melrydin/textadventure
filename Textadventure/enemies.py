# -*- coding: utf-8 -*-

from inventory import game_inventory
from items.items import potion_list

# basic commands for Player and Enemies
class Character:
    def __init__(self, name, level, hp, attack):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack

        
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
    def __init__(self, name, level, hp, attack, mana, endurance):
        Character.__init__(self, name, level, hp, attack)
        self.max_hp = hp
        self.mana = mana
        self.max_mana = mana
        self.endurance = endurance
        self.max_endurance = endurance
        
    def die(self):
        exit("Du bist gestorben. Versuchs nochmal.")
        
    def rest(self):
        if self.hp < self.max_hp:
            self.hp = self.hp + (self.max_hp * 0.1)
            if self.hp > self.max_hp:
                self.hp = self.max_hp
                
    # drink Potion     
    def drink(self, item_number):
        for potion_art in potion_list:
            for potion in potion_art:
                if game_inventory[int(item_number)-1] == potion:
                    if game_inventory[int(item_number)-1].name[:6] == "Health":
                        self.hp = self.hp + game_inventory[int(item_number)-1].regenerated_health
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        print("Du hast nun wieder " + str(int(self.hp)) + " HP")  
                    elif game_inventory[int(item_number)-1].name[:9] == "Endurance":
                        self.endurance = self.endurance + game_inventory[int(item_number)-1].regenerated_endurance
                        if self.endurance > self.max_endurance:
                            self.endurance = self.max_endurance
                        print("Du hast nun wieder " + str(int(self.endurance)) + " Ausdauer")
                    elif game_inventory[int(item_number)-1].name[:4] == "Mana":
                        self.mana = self.mana + game_inventory[int(item_number)-1].regenerated_mana
                        if self.mana > self.max_mana:
                            self.mana = self.max_mana
                        print("Du hast nun wieder " + str(int(self.mana)) + " Mana")
                    else:
                        print("Das kann man nicht trinken")

# Goblin enemie
class Goblin(Character):
    def __init__(self):
        Character.__init__(self, "Goblin", 1, 100, 10)

# Ork enemie
class Ork(Character):
    def __init__(self):
        Character.__init__(self, "Ork", 1, 200, 20)

enemie_list = [Goblin(), Ork()]