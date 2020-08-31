# -*- coding: utf-8 -*-

from items.basic_item import basic_item

class HealthPotion():
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, regenerated_health):
        basic_item.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth)
        self.regenerated_health = regenerated_health
        
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