# -*- coding: utf-8 -*-

from random import randint
from numpy.random import choice

from items.equipment_properties import *
from items.basic_item import *
from items.consumables.potions import endurance_potion, health_potion, mana_potion

drop_list = []

potion_list = [endurance_potion.endurance_potion_list,
               health_potion.health_potion_list,
               mana_potion.mana_potion_list]

item_categorys = ["potions", "helm", "chest_armor", "belt",
                   "boot", "gloves", "pant",
                   "shield", "shoulder","amulet", 
                   "ring","sword", "axe", "mace",
                   "spear", "tow_handed_sword", 
                   "tow_handed_axe", "tow_handed_mace"]

armor_categorys = ["helm", "chest_armor", "belt",
                   "boot", "glove", "pant",
                   "shield", "shoulder"]

def property_1(level):
    stat = main_properties[randint(0, len(main_properties)-1)]
    stat_name = stat[0]
    value = randint(stat[1], stat[2]) * level
    return [stat_name, value]

def property_2(level):
    stat = primary_properties[randint(0, len(main_properties)-1)]
    stat_name = stat[0]
    value = randint(stat[1], stat[2]) * level
    return [stat_name, value]

def armor(level):
    armor = randint(5, 20) * level
    return armor
            
def drop_chance():
    items = "common","uncommon","rare","super rare"
    probabilities = [0.5,0.35,0.1,0.05]
    return str(choice(items , p=probabilities))

def item_name(equipment_category):
    name_list = []
    path = "items\Item_Name"
    name = open("{}/{}.txt".format(path, equipment_category), "r")
    for zeile in name:
        if "\n" in zeile:
            zeile = zeile[:-1]
        name_list.append(zeile)
    name.close()
    return name_list[randint(0,len(name_list)-1)]
        
# roll droop changs and loot
def loot():
    rand = 1 #randint(0,2)
    item_quantity = randint(1,3)
    if rand == 1:
        for number in range(item_quantity):
            player_level = 1
            drop_chanc_category = drop_chance()
            equipment_category = item_categorys[randint(0,len(item_categorys)-1)]
            number = 1
            if equipment_category == "potions":
                potion_category = randint(0,2)
                drop_list.append(potion_list[potion_category][randint(0, 2)])
            else:
                name = item_name(equipment_category)
                weight = 10
                worth = 10
                durability = 10
                if equipment_category in armor_categorys:
                    if drop_chanc_category == "common":
                        item = common_armor(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor(player_level), property_1(player_level))
                    elif drop_chanc_category == "uncommon":
                        item = uncommon_armor(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor(player_level), property_1(player_level), property_2(player_level))
                    elif drop_chanc_category == "rare":
                        item = rare_armor(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor(player_level), property_1(player_level), property_2(player_level), property_2(player_level))
                    elif drop_chanc_category == "super_rare":
                        item = super_rare_armor(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, armor(player_level), property_1(player_level), property_2(player_level), property_2(player_level), property_2(player_level))
                else:
                    if drop_chanc_category == "common":
                        item = common(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1(player_level))
                    elif drop_chanc_category == "uncommon":
                        item = uncommon(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1(player_level), property_2(player_level))
                    elif drop_chanc_category == "rare":
                        item = rare(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1(player_level), property_2(player_level), property_2(player_level))
                    elif drop_chanc_category == "super_rare":
                        item = super_rare(player_level, drop_chanc_category, equipment_category, number, name, weight, worth, durability, property_1(player_level), property_2(player_level), property_2(player_level), property_2(player_level))
                drop_list.append(item)