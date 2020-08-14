# -*- coding: utf-8 -*-

from items import items
from items.consumables.potions.mana_potion import mana_potion_list
from items.consumables.potions.health_potion import health_potion_list
from items.consumables.potions.endurance_potion import endurance_potion_list

class Potion(items.Item):
    def __init__(self, level, name, weight, worth):
        items.Item.__init__(self, level, name, weight, worth,)

class EndurancePotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_endurance):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_endurance = regenerated_endurance

class HealthPotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_health):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_health = regenerated_health

class ManaPotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_mana):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_mana = regenerated_mana
        
        
potion_list = [mana_potion_list, health_potion_list, endurance_potion_list]