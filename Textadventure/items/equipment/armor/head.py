# -*- coding: utf-8 -*-

from items.basic_item import common, uncommon, rare, super_rare, armor, property_1, property_2, property_3, property_4


class common_head_1(common):
    def __init__(self):
        common.__init__(self, 1, "common", "helm", 1, "Head_1", 5, 10, 10, armor(1), property_1(1))
        
class uncommon_head_1(uncommon):
    def __init__(self):
        uncommon.__init__(self, 5, "uncommon", "helm", 1, "Head_2", 5, 10, 10, armor(5), property_1(5), property_2(5))
        
class rare_head_1(rare):
    def __init__(self):
        rare.__init__(self, 5, "rare", "helm", 1, "Head_3", 5, 10, 10, armor(5), property_1(5), property_2(5), property_3(5))

class super_rare_head_1(super_rare):
    def __init__(self):
        super_rare.__init__(self, 5, "super_rare", "helm", 1, "Head_4", 5, 10, 10, armor(5), property_1(5), property_2(5), property_3(5), property_4(5))
        
common_head_list = [common_head_1()]

uncommon_head_list = [uncommon_head_1()]

rare_head_list = [rare_head_1()]

super_rare_head_list = [super_rare_head_1()]

head_dic = {"common": common_head_list,
             "uncommon": uncommon_head_list,
             "rare": rare_head_list,
             "super rare": super_rare_head_list}