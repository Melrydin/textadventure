# -*- coding: utf-8 -*-

import random

from numpy.random import choice

from items.consumables.potions.endurance_potion import endurance_potion_dic
from items.consumables.potions.health_potion import health_potion_dic
from items.consumables.potions.mana_potion import mana_potion_dic
from items.equipment.armor.head import head_dic

potion_list = [mana_potion_dic, endurance_potion_dic, health_potion_dic]

armor_non_equip_list = [head_dic]

drop_list = []
item_list = [potion_list, armor_non_equip_list]

# roll droop changs and loot
def loot():
    rand = 1 #random.randint(0,2)
    item_quantity = random.randint(1,3)
    if rand == 1:
        for number in range(item_quantity):
            item_category = item_list[random.randint(0, len(item_list) - 1)]
            item_under_category = item_category[random.randint(0, len(item_category) - 1)]
            item_rarity = item_under_category[drop_chance()]
            item = item_rarity[random.randint(0, len(item_rarity)-1)]
            drop_list.append(item)
            
def drop_chance():
    items = "common","uncommon","rare","super rare"
    probabilities = [0.5,0.35,0.1,0.05]
    return str(choice(items , p=probabilities))
