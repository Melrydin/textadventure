# -*- coding: utf-8 -*-
import random
import Items

drop_list = []

# roll droop changs and loot
def loot():
    rand = random.randint(0,2)
    item_quantity = random.randint(0,3)
    if rand == 1:
        for i in range(item_quantity):
            item_category = Items.Item_list[random.randint(0, len(Items.Item_list) - 1)]
            item = item_category[random.randint(0, len(item_category) - 1)]
            drop_list.append(item)

class Item:
    def __init__(self, weight, worth):
        self.weight = weight
        self.worth = worth
        
class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)
        
class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health        

class ManaPotion(Potion):
    def __init__(self, weight, worth, regenerated_mana):
        Potion.__init__(self, weight, worth)
        self.regenerated_mana = regenerated_mana

class EndurancePotion(Potion):
    def __init__(self, weight, worth, regenerated_endurance):
        Potion.__init__(self, weight, worth)
        self.regenerated_endurance = regenerated_endurance

armor_list = ["Copper_Armor"]
weapon_list = ["rusty_Sword"]
potion_list = ["Health_Potion"]

Item_list = [armor_list, weapon_list, potion_list]