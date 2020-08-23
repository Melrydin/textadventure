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

class head():
    def __init__(self,level, number, name, weight, worth, durability, armor, property_1, property_2, property_3):
        self.level = level
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        self.durability = durability
        self.max_durability = durability
        self.armor = armor
        self.property_1 = property_1
        self.property_2 = property_2
        self.property_3 = property_3
        
    def show_details(self):
        print(6* "-" + str(self.name) + 6* "-")
        print("Level: " + str(self.level))
        print("Armor: " + str(self.armor))
        print("Magical property: " + str(self.property_1))
        print("Magical property: " + str(self.property_2))
        print("Magical property: " + str(self.property_3))
        print("Durability: " + str(self.durability) + "/" + str(self.max_durability))
        print("Weight: " + str(self.weight))
        print("Worth: " + str(self.worth))
        
class head_1(head):
    def __init__(self):
        head.__init__(self, 1, 1, "Head_1", 5, 10, 10, armor(1), property_1(1), property_2(1), property_3(1))
        
class head_2(head):
    def __init__(self):
        head.__init__(self, 5, 1, "Head_2", 5, 10, 10, armor(5), property_1(5), property_2(5), property_3(5))
        
class head_3(head):
    def __init__(self):
        head.__init__(self, 10, 1, "Head_3", 5, 10, 10, armor(10), property_1(10), property_2(10), property_3(10))
        

head_list = [head_1(), head_2(), head_3()]