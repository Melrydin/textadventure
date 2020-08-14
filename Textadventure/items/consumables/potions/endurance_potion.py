# -*- coding: utf-8 -*-

from potions import EndurancePotion
        
class EndurancePotion_1(EndurancePotion):
    def __init__(self):
        EndurancePotion.__init__(self, 1, "EndurancPotion_1", 1, 3, 10)
    
endurance_potion_list = [EndurancePotion_1()]