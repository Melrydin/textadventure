# -*- coding: utf-8 -*-

from potions import HealthPotion
   
class HealthPotion_1(HealthPotion):
    def __init__(self):
        HealthPotion.__init__(self, 1, "HealthPotion_1", 1, 3, 10)
        
health_potion_list = [HealthPotion()]