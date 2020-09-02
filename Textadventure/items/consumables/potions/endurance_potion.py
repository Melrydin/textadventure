# -*- coding: utf-8 -*-

from items.basic_item import basic_item

class EndurancePotion(basic_item):
    def __init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth, regenerated_endurance):
        basic_item.__init__(self, level, drop_chanc_category, equipment_category, number, name, weight, worth)
        self.regenerated_endurance = regenerated_endurance

class EndurancePotion_1(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 1, "common", "Potion", 1, "EndurancePotion_1", 1, 3, 10)
        
class EndurancePotion_2(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 5, "common", "Potion", 1, "EndurancePotion_2", 1, 3, 20)
        
class EndurancePotion_3(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 10, "common", "Potion", 1, "EndurancePotion_3", 1, 3, 40)


endurance_potion_list = [EndurancePotion_1(), EndurancePotion_2(), EndurancePotion_3()]

endurance_potion_dic = {"common": endurance_potion_list,
                    "uncommon": endurance_potion_list,
                    "rare": endurance_potion_list,
                    "super rare": endurance_potion_list}