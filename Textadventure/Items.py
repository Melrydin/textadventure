# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:23:58 2020

@author: Clemens
"""
class Item:
    def __init__(self, weight, worth):
        self.weight = weight
        self.worth = worth
        
class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)
        
class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health

class ManaPotion(Potion):
    def __init__(self, weight, worth, regenerated_mana):
        Potion.__init__(self, weight, worth)
        self.regenerated_mana = regenerated_mana

class EndurancePotion(Potion):
    def __init__(self, weight, worth, regenerated_endurance):
        Potion.__init__(self, weight, worth)
        self.regenerated_endurance = regenerated_endurance