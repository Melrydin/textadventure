# -*- coding: utf-8 -*-
import random

drop_list = []

# roll droop changs and loot
def loot():
    rand = random.randint(0,2)
    item_quantity = random.randint(0,3)
    if rand == 1:
        for i in range(item_quantity):
            item_category = item_list[random.randint(0, len(item_list) - 1)]
            item = item_category[random.randint(0, len(item_category) - 1)]
            drop_list.append(item)

class Item:
    def __init__(self, level, name, weight, worth):
        self.level = level
        self.name = name
        self.weight = weight
        self.worth = worth

class Potion(Item):
    def __init__(self, level, name, weight, worth):
        Item.__init__(self, level, name, weight, worth,)
        
class HealthPotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_health):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_health = regenerated_health        

class ManaPotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_mana):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_mana = regenerated_mana

class EndurancePotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_endurance):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_endurance = regenerated_endurance
        
class EndurancePotion_1(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 1, "EndurancPotion_1", 1, 3, 10)

potion_list = [EndurancePotion_1()]

item_list = [potion_list]