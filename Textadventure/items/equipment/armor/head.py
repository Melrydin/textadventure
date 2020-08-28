# -*- coding: utf-8 -*-

import random

def armor(level):
    armor_value = random.randint(5, 20) * level
    return armor_value
    
def property_1(level):
    return("Proberty_1")

def property_2(level):
    return("Proberty_2")

def property_3(level):
    return("Proberty_3")

def property_4(level):
    return("Proberty_4")

class helm():
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1):
        self.level = level
        self.drop_chanc_category = drop_chanc_category
        self.equipment_category = equipment_category
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        self.durability = durability
        self.max_durability = durability
        self.armor = armor
        self.property_1 = property_1
        
    def show_details(self):
        print(6* "-" + str(self.name) + 6* "-")
        print("Level: " + str(self.level))
        print("Ausrüstungs_Seltenheit: " + str(self.drop_chanc_category))
        print("Kategorie: " + str(self.equipment_category))
        print("Armor: " + str(self.armor))
        print("Magical property: " + str(self.property_1))
        print("Magical property: " + str(self.property_2))
        print("Magical property: " + str(self.property_3))
        print("Durability: " + str(self.durability) + "/" + str(self.max_durability))
        print("Weight: " + str(self.weight))
        print("Worth: " + str(self.worth))
        
class uncommon(helm):
    def __init__(self, level, drop_chanc_category,equipment_category, number, name, weight, worth, durability, armor, property_1, property_2):
        helm.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1)
        self.property_2 = property_2
        
class rare(uncommon):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1, property_2, property_3):
        uncommon.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1,  property_2)
        self.property_3 = property_3

class super_rare(rare):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1, property_2, property_3, property_4):
        rare.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1,  property_2, property_3)
        self.property_4 = property_4        

# -------------------------------------------------------------------- Items --------------------------------------------------------------------

class common_head_1(helm):
    def __init__(self):
        helm.__init__(self, 1, "common", "Helm", 1, "Head_1", 5, 10, 10, armor(1), property_1(1))
        
class uncommon_head_1(uncommon):
    def __init__(self):
        uncommon.__init__(self, 5, "uncommon", "Helm", 1, "Head_2", 5, 10, 10, armor(5), property_1(5), property_2(5))
        
class rare_head_1(rare):
    def __init__(self):
        rare.__init__(self, 10, "rare", "Helm", 1, "Head_3", 5, 10, 10, armor(10), property_1(10), property_2(10), property_3(10))

class super_rare_head_1(super_rare):
    def __init__(self):
        super_rare.__init__(self, 1, "super_rare", "Helm", 1, "Head_4", 5, 10, 10, armor(1), property_1(1), property_2(1), property_3(1), property_4(1))
        
common_head_list = [common_head_1()]

uncommon_head_list = [uncommon_head_1()]

rare_head_list = [rare_head_1()]

super_rare_head_list = [super_rare_head_1()]

head_dic = {"common": common_head_list,
             "uncommon": uncommon_head_list,
             "rare": rare_head_list,
             "super rare": super_rare_head_list}