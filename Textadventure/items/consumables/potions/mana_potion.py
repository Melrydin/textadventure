# -*- coding: utf-8 -*-

class ManaPotion():
    def __init__(self, level, equipment_category, number, name, weight, worth, regenerated_mana):
        self.regenerated_mana = regenerated_mana
        self.level = level
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        self.equipment_category = equipment_category
        
    def number_counter_plus(self):
        self.number = self.number + 1
        
    def number_counter_minus(self):
        self.number = self.number - 1
    
    def show_details(self):
        print(6* "-" + str(self.name) + 6* "-")
        print("Level: " + str(self.level))
        print("Kategorie: " + str(self.equipment_category))
        print("Number: " + str(self.number))
        print("Mana regeneration: " + str(self.regenerated_mana))
        print("Weight: " + str(self.weight))
        print("Worth: " + str(self.worth))
        
class ManaPotion_1(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 1, "common", 1, "ManaPotion_1", 1, 3, 10)

class ManaPotion_2(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 5, "common", 1, "ManaPotion_2", 1, 3, 20)
        
class ManaPotion_3(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 10, "common", 1, "ManaPotion_3", 1, 3, 40)
        
mana_potion_list = [ManaPotion_1(), ManaPotion_2(), ManaPotion_3()]
        
mana_potion_dic = {"common": mana_potion_list,
                    "uncommon": mana_potion_list,
                    "rare": mana_potion_list,
                    "super rare": mana_potion_list}

