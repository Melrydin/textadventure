# -*- coding: utf-8 -*-

from items.basic_item import common, uncommon, rare, super_rare, property_1, property_2, property_3, property_4

class common_ring_1(common):
    def __init__(self):
        common.__init__(self, 1, "common", "ring", 1, "Ring_1", 5, 10, 10, property_1(1))
        
class uncommon_ring_1(uncommon):
    def __init__(self):
        uncommon.__init__(self, 5, "uncommon", "ring", 1, "Ring_2", 5, 10, 10, property_1(5), property_2(5))
        
class rare_ring_1(rare):
    def __init__(self):
        rare.__init__(self, 5, "rare", "ring", 1, "Ring_3", 5, 10, 10, property_1(5), property_2(5), property_3(5))

class super_rare_ring_1(super_rare):
    def __init__(self):
        super_rare.__init__(self, 5, "super_rare", "ring", 1, "Ring_4", 5, 10, 10, property_1(5), property_2(5), property_3(5), property_4(5))


common_ring_list = [common_ring_1()]

uncommon_ring_list = [uncommon_ring_1()]

rare_ring_list = [rare_ring_1()]

super_rare_ring_list = [super_rare_ring_1()]

ring_dic = {"common": common_ring_list,
             "uncommon": uncommon_ring_list,
             "rare": rare_ring_list,
             "super rare": super_rare_ring_list}