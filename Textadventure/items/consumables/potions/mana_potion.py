# -*- coding: utf-8 -*-

from items.consumables.potions.potions import ManaPotion

class ManaPotion_1(ManaPotion):
    def __init__(self):
        ManaPotion.__init__(self, 1, "EndurancPotion_1", 1, 3, 10)
        
mana_potion_list = [ManaPotion_1()]