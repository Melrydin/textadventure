# -*- coding: utf-8 -*-

armor_categorys = ["helm", "chest_armor", "belt",
                   "boot", "glove", "pant",
                   "shield", "shoulder"]
    
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
        print("------ {} ------".format(self.name))
        print("Item Level: {}".format(self.level))
        print("Kategorie: {}".format(self.equipment_category))
        if self.equipment_category != "Potion":
            print("Ausrüstungs_Seltenheit: {}".format(self.drop_chanc_category))
            if self.equipment_category in [armor_categorys]:
                print("Armor: {}".format(self.armor))
            print("Magical property: {} {}".format(self.property_1[0],self.property_1[1]))
            if self.drop_chanc_category in ["uncommon", "rara", "super_rare"]:
                print("Magical property: {} {}".format(self.property_2[0],self.property_2[1]))
            if self.drop_chanc_category in ["rare", "super_rare"]:
                print("Magical property: {} {}".format(self.property_3[0],self.property_3[1]))
            if self.drop_chanc_category == "super_rare":
                print("Magical property: {} {}".format(self.property_4[0],self.property_4[1]))
            print("Durability: {}/{}".format(self.durability,self.max_durability))
        else:
            if "Enduranc" in self.name:
                print("Endurance regeneration: {}".format(self.regenerated_endurance))
            elif "Mana" in self.name:
                print("Mana regeneration: {}".format(self.regenerated_mana))
            elif "Health" in self.name:
                print("Health regeeneration: {}".format(self.regenerated_health))
        print("Weight: {}".format(self.weight))
        print("Worth: {}".format(self.worth))
            
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
        self.property_3 = property_2

class super_rare(rare):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1, property_2, property_3, property_4):
        rare.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1,  property_2, property_3)
        self.property_4 = property_2
        
class common_armor(common):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1):
        common.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1)
        self.armor = armor
        
class uncommon_armor(uncommon):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor, property_1, property_2):
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