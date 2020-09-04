# -*- coding: utf-8 -*-

from items.basic_item import common, uncommon, rare, super_rare, property_1, property_2, property_3, property_4

class common_amulet_1(common):
    def __init__(self):
        common.__init__(self, 1, "common", "amulet", 1, "Amulet_1", 5, 10, 10, property_1(1))
        
class uncommon_amulet_1(uncommon):
    def __init__(self):
        uncommon.__init__(self, 5, "uncommon", "amulet", 1, "Amulet_2", 5, 10, 10, property_1(5), property_2(5))
        
class rare_amulet_1(rare):
    def __init__(self):
        rare.__init__(self, 5, "rare", "amulet", 1, "Amulet_3", 5, 10, 10, property_1(5), property_2(5), property_3(5))

class super_rare_amulet_1(super_rare):
    def __init__(self):
        super_rare.__init__(self, 5, "super_rare", "amulet", 1, "Amulet_4", 5, 10, 10, property_1(5), property_2(5), property_3(5), property_4(5))


common_amulet_list = [common_amulet_1()]

uncommon_amulet_list = [uncommon_amulet_1()]

rare_amulet_list = [rare_amulet_1()]

super_rare_amulet_list = [super_rare_amulet_1()]

amulet_dic = {"common": common_amulet_list,
             "uncommon": uncommon_amulet_list,
             "rare": rare_amulet_list,
             "super rare": super_rare_amulet_list}