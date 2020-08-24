# -*- coding: utf-8 -*-

class EndurancePotion():
    def __init__(self, level, equipment_category, number, name, weight, worth, regenerated_endurance):
        self.regenerated_endurance = regenerated_endurance
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
        print("Endurance regeneration: " + str(self.regenerated_endurance))
        print("Weight: " + str(self.weight))
        print("Worth: " + str(self.worth))

class EndurancePotion_1(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 1, "common", 1, "EndurancePotion_1", 1, 3, 10)
        
class EndurancePotion_2(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 5, "common", 1, "EndurancePotion_2", 1, 3, 20)
        
class EndurancePotion_3(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 10, "common", 1, "EndurancePotion_3", 1, 3, 40)
    
endurance_potion_list = [EndurancePotion_1(), EndurancePotion_2(), EndurancePotion_3()]

endurance_potion_dic = {"common": endurance_potion_list,
                    "uncommon": endurance_potion_list,
                    "rare": endurance_potion_list,
                    "super rare": endurance_potion_list}