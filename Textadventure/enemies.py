# -*- coding: utf-8 -*-

from inventory import game_inventory
from items.items import potion_list

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
                
    # drink Potion     
    def drink(self, item_number):
        for i in potion_list:
            for j in i:
                if game_inventory[int(item_number)-1] == j:
                    if game_inventory[int(item_number)-1].name[:6] == "Health":
                        self.hp = self.hp + game_inventory[int(item_number)-1].regenerated_health
                        print("Du hast nun wieder " + str(int(self.hp)) + " HP")
                        
                    elif game_inventory[int(item_number)-1].name[:9] == "Endurance":
                        self.endurance = self.endurance + game_inventory[int(item_number)-1].regenerated_endurance
                        print("Du hast nun wieder " + str(int(self.endurance)) + " Ausdauer")
                        
                    elif game_inventory[int(item_number)-1].name[:4] == "Mana":
                        self.mana = self.mana + game_inventory[int(item_number)-1].regenerated_mana
                        print("Du hast nun wieder " + str(int(self.mana)) + " Mana")
                        
                    else:
                        print("Das kann man nicht trinken")
        if game_inventory[int(item_number)-1].number > 1:
            game_inventory[int(item_number)-1].number_counter_minus()
        else:
            del game_inventory[int(item_number)-1]

# Goblin enemie
class Goblin(Character):
    def __init__(self):
        Character.__init__(self, "Goblin", 100, 10)

# Ork enemie
class Ork(Character):
    def __init__(self):
        Character.__init__(self, "Ork", 200, 20)

enemie_list = [Goblin(), Ork()]