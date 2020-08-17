# -*- coding: utf-8 -*-

class Potion():
    def __init__(self, level, name, weight, worth):
        self.level = level
        self.name = name
        self.weight = weight
        self.worth = worth

class HealthPotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_health):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_health = regenerated_health
   
class HealthPotion_1(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 1, "HealthPotion_1", 1, 3, 10)
        
health_potion_list = [HealthPotion_1()]