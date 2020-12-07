# -*- coding: utf-8 -*-

from enemies import player

player_stats_dic = {"name": player.name, 
                    "level": 0,
                    "live": player.hp,
                    "strength": 0,
                    "intelligence": 0,
                    "dexterity": 0,
                    "vitality": 0,
                    "critical_hit_chance": 0,
                    "critical_hit_danage": 0,
                    "dodge_chance": 0,
                    "armor": 0,
                    "physical_resistance": 0,
                    "cold_resistance": 0,
                    "fire_resistance": 0,
                    "lightning_resistance": 0,
                    "poison_resistance": 0,
                    "arcan_holy_resistance": 0,
                    "total_life_bonus": 0,
                    "life_per_hit": 0,
                    "life_per_kill": 0,
                    "resource_cost_reduction": 0,
                    "gold_find": 0,
                    "magic_find": 0,
                    "bonus_experience": 0}

def print_player():
    print(6*"-" + "Your Stats" + 6*"-")
    print("Name: " + player_stats_dic["name"])
    print("Level: " + player_stats_dic["level"])
    print("Live: " + player_stats_dic["live"])
    print("Stringth: " + player_stats_dic["strength"])
    print("Intelligence: " + player_stats_dic["intelligence"])
    print("Dexterity: " + player_stats_dic["dexterity"])
    print("Vitality: " + player_stats_dic["vitality"])
    print("Critical Hit Chance: " + player_stats_dic["critical_hit_chance"])
    print("Critical Hit Danage: " + player_stats_dic["critical_hit_danage"])
    print("Doge Chance: " + player_stats_dic["dodge_chance"])
    print("Armor: " + player_stats_dic["armor"])
    print("Physical Resistance: " + player_stats_dic["physical_resistance"])
    print("Cold Resistance: " + player_stats_dic["cold_resistance"])
    print("Fire Resistance: " + player_stats_dic["fire_resistance"])
    print("Lightning Resistance: " + player_stats_dic["lightning_resistance"])
    print("Poison Resistance: " + player_stats_dic["poison_resistance"])
    print("Arcan Holy Resistance: " + player_stats_dic["arcan_holy_resistance"])
    print("Total Life Bonus: " + player_stats_dic["total_life_bonus"])
    print("Life per Hit: " + player_stats_dic["life_per_hit"])
    print("Life per Kill: " + player_stats_dic["life_per_kill"])
    print("Resource cost Reduction: " + player_stats_dic["resource_cost_reduction"])
    print("Gold find: " + player_stats_dic["gold_find"])
    print("Magic find: " + player_stats_dic["magic_find"])
    print("Bonus Experience: " + player_stats_dic["bonus_experience"])