# -*- coding: utf-8 -*-

# name, min, max, classe_speziefisch, item vergleich, item speziefische stats

main_properties_item_stats = ["helm", "chest_armor", "belt",
                              "boot", "glove", "pant","shield",
                              "shoulder","amulet", "ring", "sword", "axe", "mace",
                              "spear", "tow_handed_sword", "tow_handed_axe",
                              "tow_handed_mace"]

main_properties = [["Dexterity", 5, 100, None, True, main_properties_item_stats],
                   ["Strength", 5, 100, None, True, main_properties_item_stats],
                   ["Intelligence", 5, 100, None, True, main_properties_item_stats],
                   ["Vitality", 5, 100, None, True, main_properties_item_stats]]

primary_properties = [["Critical hit Chance", 5, 10, None, True, ["glove","amulet", "ring","helm"]],
                      ["Critical hit Danage", 25, 50, None, True, [""]],
                      ["Dodge Chance", 0, 10, None, True, [""]],
                      ["Armor", 100, 250, None, True, [""]],
                      ["Total Life Bonus", 10, 15, None, True, [""]],
                      ["Resource Cost Reduction", 8, 10, None, True, [""]]]

                       
sekunder_properties = [["Physical Resistance", 50, 100, None, True, [""]],
                       ["Cold Resistance", 50, 100, None, True, [""]],
                       ["Fire Resistance", 50, 100, None, True, [""]],
                       ["Lightning Resistance", 50, 100, None, True, [""]],
                       ["Poison Resistance", 50, 100, None, True, [""]],
                       ["Arcan/Holy Resistance", 50, 100, None, True, [""]],
                       ["Life per Hit", 50, 100, None, True, [""]],
                       ["Life per Kill", 50, 100, None, True, [""]],
                       ["Gold Find", 50, 100, None, True, [""]],
                       ["Magic Find", 50, 100, None, True, [""]],
                       ["Bonus Experience", 50, 100, None, True, [""]]]
