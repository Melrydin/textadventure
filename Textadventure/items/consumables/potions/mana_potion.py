# -*- coding: utf-8 -*-

from items.basic_item import basic_item

class ManaPotion(basic_item):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, regenerated_mana):
        basic_item.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth)
        self.regenerated_mana = regenerated_mana
        
class ManaPotion_1(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 1, "common", "Potion", 1, "ManaPotion_1", 1, 3, 10)

class ManaPotion_2(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 5, "common", "Potion", 1, "ManaPotion_2", 1, 3, 20)
        
class ManaPotion_3(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 10, "common", "Potion", 1, "ManaPotion_3", 1, 3, 40)
        
mana_potion_list = [ManaPotion_1(), ManaPotion_2(), ManaPotion_3()]
        
mana_potion_dic = {"common": mana_potion_list,
                    "uncommon": mana_potion_list,
                    "rare": mana_potion_list,
                    "super rare": mana_potion_list}

