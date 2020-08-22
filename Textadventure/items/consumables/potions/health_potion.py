# -*- coding: utf-8 -*-

class HealthPotion():
    def __init__(self, level, number, name, weight, worth, regenerated_health):
        self.regenerated_health = regenerated_health
        self.level = level
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        
    def number_counter_plus(self):
        self.number = self.number + 1
        
    def number_counter_minus(self):
        self.number = self.number - 1
        
class HealthPotion_1(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 1, 1, "HealthPotion_1", 1, 3, 10)

class HealthPotion_2(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 5, 1, "HealthPotion_2", 1, 3, 20)

class HealthPotion_3(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 10, 1, "HealthPotion_3", 1, 3, 40)
        
health_potion_list = [HealthPotion_1(), HealthPotion_2(), HealthPotion_3()]