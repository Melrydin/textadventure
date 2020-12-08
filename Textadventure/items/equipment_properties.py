# -*- coding: utf-8 -*-

# name, min, max, classe_speziefisch, item vergleich, item speziefische stats

main_properties_item_stats = ["helm", "chest_armor", "belt",
                              "boot", "glove", "pant","shield",
                              "shoulder","amulet", "ring", "sword", "axe", "mace",
                              "spear", "tow_handed_sword", "tow_handed_axe",
                              "tow_handed_mace"]

armor_categorys = ["helm", "chest_armor", "belt",
                   "boot", "glove", "pant",
                   "shield", "shoulder"]

main_properties = [["Dexterity", 5, 100, None, True, main_properties_item_stats],
                   ["Strength", 5, 100, None, True, main_properties_item_stats],
                   ["Intelligence", 5, 100, None, True, main_properties_item_stats],
                   ["Vitality", 5, 100, None, True, main_properties_item_stats]]

primary_properties = [["Critical hit Chance", 5, 10, None, True, ["glove","amulet", "ring","helm"]],
                      ["Critical hit Danage", 25, 50, None, True, ["glove","amulet", "ring"]],
                      ["Dodge Chance", 0, 10, None, True, ["shield"]],
                      ["Armor", 100, 250, None, True, armor_categorys],
                      ["Total Life Bonus", 10, 15, None, True, ["helm", "chest_armor", "shoulder"]],
                      ["Resource Cost Reduction", 8, 10, None, True, ["glove", "pant","shield", "shoulder","amulet", "ring", "sword", "axe", "mace", "spear", "tow_handed_sword", "tow_handed_axe", "tow_handed_mace"]]]

                       
sekunder_properties = [["Physical Resistance", 50, 100, None, True, [main_properties_item_stats]],
                       ["Cold Resistance", 50, 100, None, True, [main_properties_item_stats]],
                       ["Fire Resistance", 50, 100, None, True, [main_properties_item_stats]],
                       ["Lightning Resistance", 50, 100, None, True, [main_properties_item_stats]],
                       ["Poison Resistance", 50, 100, None, True, [main_properties_item_stats]],
                       ["Arcan/Holy Resistance", 50, 100, None, True, [main_properties_item_stats]],
                       ["Life per Hit", 50, 100, None, True, [main_properties_item_stats]],
                       ["Life per Kill", 50, 100, None, True, [main_properties_item_stats]],
                       ["Gold Find", 50, 100, None, True, [main_properties_item_stats]],
                       ["Magic Find", 50, 100, None, True, [main_properties_item_stats]],
                       ["Bonus Experience", 50, 100, None, True, [main_properties_item_stats]]]
