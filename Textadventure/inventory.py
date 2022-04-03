# -*- coding: utf-8 -*-

from items.items import drop_list

game_inventory = []

armor_categorys = ["helm", "chest_armor", "belt",
                   "boot", "glove", "pant",
                   "shield", "shoulder"]

non_armor_categorys = ["amulet", "ring"]

weapon_categorys = ["sword", "axe", "mace",
                    "spear", "tow_handed_sword", "tow_handed_axe",
                    "tow_handed_mace"]
armor_list = []
non_armor_list = []
weapon_list = []

equip_list = [armor_list,non_armor_list,weapon_list]

# pick up items and stow them in your inventory
def pickup(player, maps):
    for i in range(len(drop_list)):
        # stacking double Items
        if drop_list[i] in game_inventory:    
            if "Potion" in drop_list[i].name:
                game_inventory[game_inventory.index(drop_list[i])].number_counter_plus()
            else:
                game_inventory.append(drop_list[i])
        else:
            game_inventory.append(drop_list[i])
    drop_list.clear()
    # sort inventory to name
    game_inventory.sort(key=lambda item: item.name, reverse=True)

# look in your inventory
def inventory(player, maps):
    print("Gib \"hilfe\" ein um eine uebersicht der Inventar Befehle zu erhalten.\n")
    len_game_inventory = len(game_inventory)
    for i in range(len_game_inventory):
        inventory_Commands.update({str(int(i)):senseless})
    while True:
        print("")
        print(6* "-" + "Inventory" + 6* "-")
        for i in range(len(game_inventory)):
            print("{}: {}x{}".format(i,game_inventory[i].number,game_inventory[i].name))
        inventory_command = input("Inventory >>>").lower().split(" ")
        if inventory_command[0] in inventory_Commands:
            if len(inventory_command) > 1:
                inventory_Commands[inventory_command[1]](player, inventory_command[0])
            elif len(inventory_command) == 1:
                inventory_Commands[inventory_command[0]]()
            else:
                senseless()
        elif inventory_command[0] == "quit":
            break
        else:
            senseless()
    for i in range(len_game_inventory):
        inventory_Commands.pop(str(i), None)

# equip equipment
def equip(player, item_number):
    # Is it an item, an armor item
    if game_inventory[int(item_number)].equipment_category in armor_categorys:
        equip_c(armor_list, item_number)
    # Is it an item, an ring
    elif game_inventory[int(item_number)].equipment_category == "ring":
        ring_list = []
        ring_number(ring_list, item_number)
    # Is it an item, an non armor item
    elif game_inventory[int(item_number)].equipment_category in non_armor_categorys:
        equip_c(non_armor_list, item_number)
    # Is it an item, an Weapon item
    elif game_inventory[int(item_number)].equipment_category in weapon_categorys:
        equip_c(weapon_list, item_number)
    # Is it an item for equip
    else:
        print("Das kann man nicht anziehen")
    # sort inventory to name
    game_inventory.sort(key=lambda item: item.name, reverse=True)

def equip_c(equip_ca, item_number):
    # The list is greater than one
    if len(equip_ca) > 0:
        for item in equip_ca:
            # Is an item of the same category in the list
            if item.equipment_category == game_inventory[int(item_number)].equipment_category:
                # Append item from equip_ca to game_inventory
                game_inventory.append(equip_ca[equip_ca.index(item)])
                del equip_ca[equip_ca.index(item)]
                equip_ca.append(game_inventory[int(item_number)])
                del game_inventory[int(item_number)]
                break
    else:    
        equip_ca.append(game_inventory[int(item_number)])
        del game_inventory[int(item_number)]      

# disarm equipment
def disarm(player, equipment_category):
    for e_cat in equip_list:
        for equipment in e_cat:
            if equipment.equipment_category == equipment_category:
                game_inventory.append(equipment)
                e_cat.remove(equipment)
    # sort inventory to name
    game_inventory.sort(key=lambda item: item.name, reverse=True)

# equip rings
def ring_number(ring_list, item_number):
    # delete ring from the non_armor_list and attach it to the ring_list
    for item in non_armor_list:
        if item.equipment_category == "Ring":
            ring_list.append(item)
            non_armor_list.remove(item)
    # ring_list is full 
    if len(ring_list) == 2:
        for i in range(len(ring_list)):
            for ring in ring_list:
                print(str(i) + ": " + ring.name)
        ring_n = input("Ring Nummer: ")
        game_inventory.append(ring_list[ring_n])
        del ring_list[ring_n]
        # Append item from equip_ca to game_inventory
        ring_list.append(game_inventory[int(item_number)])
        del game_inventory[int(item_number)]
    else:    
        ring_list.append(game_inventory[int(item_number)])
        del game_inventory[int(item_number)]
    # attach it a rings from ring_list to non_armor_list
    for ring in ring_list:
        non_armor_list.append(ring)
    ring_list.clear

# disassemble equipment or Potion
def disassemble(player, item_number):
    pass

# drink potions
def drink(player, item_number):
    # call drink function in player from enemies modull
    player.drink(item_number)
    if game_inventory[int(item_number)].number > 1:
        game_inventory[int(item_number)].number_counter_minus()
    else:
        del game_inventory[int(item_number)]
    # sort inventory to name
    game_inventory.sort(key=lambda item: item.name, reverse=True)

# show item Details
def details(player, item_number):
    return game_inventory[int(item_number)].show_details()
        
# senseless action
def senseless():
    print("Was tuhst du da? Du wuehlst Sinnlos in deiner Tasche.")
    
# print invrntory Commsnds
def print_help():
    for i in range(len(game_inventory)):
        inventory_Commands.pop(str(i), None)
    for i in inventory_Commands:
        print(i)
    print("quit")
    for i in range(len(game_inventory)):
        inventory_Commands.update({str(i):i})

# Player inventory Commands
inventory_Commands = {
    "hilfe": print_help,
    "equip": equip,
    "disarm": disarm,
    "drink": drink,
    "disassemble": disassemble,
    "details": details,
    "---disarm---": senseless,
    "helm": senseless,
    "chest_armor": senseless,
    "belt": senseless,
    "boot": senseless,
    "glove": senseless,
    "pant": senseless,
    "shield": senseless, 
    "shoulder": senseless,
    "amulet": senseless, 
    "ring": senseless, 
    "sword": senseless, 
    "axe": senseless, 
    "mace": senseless,
    "spear": senseless,
    "tow_handed_sword": senseless, 
    "tow_handed_axe": senseless,
    "tow_handed_mace": senseless}
