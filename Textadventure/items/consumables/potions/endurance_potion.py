# -*- coding: utf-8 -*-

class Potion():
    def __init__(self, level, name, weight, worth):
        self.level = level
        self.name = name
        self.weight = weight
        self.worth = worth

class EndurancePotion(Potion):
    def __init__(self, level, name, weight, worth, regenerated_endurance):
        Potion.__init__(self, level, name, weight, worth)
        self.regenerated_endurance = regenerated_endurance
        
class EndurancePotion_1(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 1, "EndurancPotion_1", 1, 3, 10)
    
endurance_potion_list = [EndurancePotion_1()]