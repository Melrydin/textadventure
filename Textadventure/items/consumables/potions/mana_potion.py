# -*- coding: utf-8 -*-

class Potion():
    def __init__(self, level, name, weight, worth):
        self.level = level
        self.name = name
        self.weight = weight
        self.worth = worth

class ManaPotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_mana):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_mana = regenerated_mana

class ManaPotion_1(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 1, "EndurancPotion_1", 1, 3, 10)
        
mana_potion_list = [ManaPotion_1()]