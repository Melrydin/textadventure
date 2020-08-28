# -*- coding: utf-8 -*-

class HealthPotion():
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, regenerated_health):
        self.regenerated_health = regenerated_health
        self.level = level
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        self.equipment_category = equipment_category
        self.drop_chanc_category = drop_chanc_category
        
    def number_counter_plus(self):
        self.number = self.number + 1
        
    def number_counter_minus(self):
        self.number = self.number - 1
        
    def show_details(self):
        print(6* "-" + str(self.name) + 6* "-")
        print("Level: " + str(self.level))
        print("Ausrüstungs_Seltenheit: " + str(self.drop_chanc_category))
        print("Kategorie: " + str(self.equipment_category))
        print("Number: " + str(self.number))
        print("Heakth regeneration: " + str(self.regenerated_health))
        print("Weight: " + str(self.weight))
        print("Worth: " + str(self.worth))
        
class HealthPotion_1(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 1, "common", "Potion", 1, "HealthPotion_1", 1, 3, 10)

class HealthPotion_2(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 5, "common", "Potion", 1, "HealthPotion_2", 1, 3, 20)

class HealthPotion_3(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 10, "common", "Potion", 1, "HealthPotion_3", 1, 3, 40)
        
health_potion_list = [HealthPotion_1(), HealthPotion_2(), HealthPotion_3()]

health_potion_dic = {"common": health_potion_list,
                    "uncommon": health_potion_list,
                    "rare": health_potion_list,
                    "super rare": health_potion_list}