# -*- coding: utf-8 -*-

from random import randint
from .equipment_properties import *


armor_categorys = ["helm", "chest_armor", "belt",
                   "boot", "glove", "pant",
                   "shield", "shoulder"]

def armor(level):
    armor_value = randint(5, 20) * level
    return armor_value
    
def property_1(level):
    stat = main_properties[randint(0, len(main_properties)-1)]
    stat_name = stat[0]
    value = randint(stat[1], stat[2]) * level
    return [stat_name, value]

def property_2(level):
    stat = main_properties[randint(0, len(main_properties)-1)]
    stat_name = stat[0]
    value = randint(stat[1], stat[2]) * level
    return [stat_name, value]

def property_3(level):
    stat = primary_properties[randint(0, len(main_properties)-1)]
    stat_name = stat[0]
    value = randint(stat[1], stat[2]) * level
    return [stat_name, value]

def property_4(level):
    stat = primary_properties[randint(0, len(main_properties)-1)]
    stat_name = stat[0]
    value = randint(stat[1], stat[2]) * level
    return [stat_name, value]

class basic_item():
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth):
        self.level = level
        self.drop_chanc_category = drop_chanc_category
        self.equipment_category = equipment_category
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        
    def number_counter_plus(self):
        self.number = self.number + 1
        
    def number_counter_minus(self):
        self.number = self.number - 1
        
    def show_details(self):
        print(6* "-" + str(self.name) + 6* "-")
        print("Item Level: " + str(self.level))
        print("Ausrüstungs_Seltenheit: " + str(self.drop_chanc_category))
        print("Kategorie: " + str(self.equipment_category))
        if self.equipment_category in [armor_categorys]:
            print("Armor: " + str(self.armor))
        if self.equipment_category != "Potion":
            print("Magical property: " + self.property_1[0] + " " + str(self.property_1[1]))
            if self.drop_chanc_category in ["uncommon", "rara", "super_rare"]:
                print("Magical property: " + self.property_2[0] + " " + str(self.property_2[1]))
            if self.drop_chanc_category in ["rare", "super_rare"]:
                print("Magical property: " + self.property_3[0] + " " + str(self.property_3[1]))
            if self.drop_chanc_category == "super_rare":
                print("Magical property: " + self.property_4[0] + " " + str(self.property_4[1]))
            print("Durability: " + str(self.durability) + "/" + str(self.max_durability))
        else:
            if "Enduranc" in self.name:
                print("Endurance regeneration: " + str(self.regenerated_endurance))
            elif "Mana" in self.name:
                print("Mana regeneration: " + str(self.regenerated_mana))
            elif "Health" in self.name:
                print("Health regeeneration: " + str(self.regenerated_health))
        print("Weight: " + str(self.weight))
        print("Worth: " + str(self.worth))
            
class common(basic_item):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1):
        basic_item.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth)
        self.property_1 = property_1
        self.durability = durability
        self.max_durability = durability
        
class uncommon(common):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1, property_2):
        common.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1)
        self.property_2 = property_2
        
class rare(uncommon):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1, property_2, property_3):
        uncommon.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1,  property_2)
        self.property_3 = property_3

class super_rare(rare):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1, property_2, property_3, property_4):
        rare.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1,  property_2, property_3)
        self.property_4 = property_4
        
class common_armor(common):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1):
        common.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1)
        self.armor = armor
        
class uncommon_armor(uncommon):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armnor, property_1, property_2):
        uncommon.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1, property_2)
        self.armor = armor
        
class rare_armor(rare):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1, property_2, property_3):
        rare.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1,  property_2, property_3)
        self.armor = armor
        
class super_rare_armor(super_rare):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1, property_2, property_3, property_4):
        super_rare.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1,  property_2, property_3, property_4)
        self.armor = armor