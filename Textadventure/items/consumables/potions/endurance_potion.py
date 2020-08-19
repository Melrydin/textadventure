# -*- coding: utf-8 -*-

class EndurancePotion():
    def __init__(self, level, number, name, weight, worth, regenerated_endurance):
        self.regenerated_endurance = regenerated_endurance
        self.level = level
        self.number = number
        self.name = name
        self.weight = weight
        self.worth = worth
        
    def number_counter(self):
        self.number = self.number + 1

        
class EndurancePotion_1(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 1, 1, "EndurancPotion_1", 1, 3, 10)
        
class EndurancePotion_2(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 5, 1, "EndurancPotion_2", 1, 3, 20)
        
class EndurancePotion_3(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 10, 1, "EndurancPotion_3", 1, 3, 40)
    
endurance_potion_list = [EndurancePotion_1(), EndurancePotion_2(), EndurancePotion_3()]