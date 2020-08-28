# -*- coding: utf-8 -*-

from items.items import drop_list

game_inventory = []

armor_categorys = ["Helm", "Chest Armor", "Belt",
                   "Boot", "Glove", "Pant",
                   "Shield", "Shoulder"]

non_armor_categorys = ["Amulet", "Ring"]

weapon_categorys = ["Sword", "Axe", "Mace",
                    "Spear", "Tow-Handed Sword", "Tow-Handed Axe",
                    "Tow-Handed Mace"]

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
    print(6* "-" + "Inventory" + 6* "-")
    for i in range(len(game_inventory)):
        print(str(i+1) + ": " + str(game_inventory[i].number) + "x" + game_inventory[i].name)
        inventory_Commands.update({str(int(i)+1):senseless})
    while True:
        inventory_command = input("Inventory >>>").lower().split(" ")
        if inventory_command[0] in inventory_Commands:
            if len(inventory_command) > 1:
                inventory_Commands[inventory_command[1]](player, inventory_command[0])
            else:
                inventory_Commands[inventory_command[0]]()
        elif inventory_command[0] == "quit":
            break
        else:
            senseless()
        print("")
        print(6* "-" + "Inventory" + 6* "-")
        for i in range(len(game_inventory)):
            print(str(i+1) + ": " + str(game_inventory[i].number) + "x" + game_inventory[i].name)
    for i in range(len(game_inventory)):
        inventory_Commands.pop(str(i), None)

# equip equipment
def equip(player, item_number):
    # Is it an item, an armor item
    if game_inventory[int(item_number)].equipment_category in armor_categorys:
        equip_c(armor_list, item_number)
    # Is it an item, an non armor item
    elif game_inventory[int(item_number)].equipment_category in non_armor_categorys:
        equip_c(non_armor_list, item_number)
    # Is it an item, an Weapon item
    elif game_inventory[int(item_number)].equipment_category in weapon_categorys:
        equip_c(weapon_list, item_number)
    # Is it an item for equip
    else:
        print("Das kann man nicht anziehen")

def equip_c(equip_ca, item_number):
    # The list is greater than one
    if len(equip_ca) > 0:
        for item in equip_ca:
            # Is an item of the same category in the list
            if item.equipment_category == game_inventory[int(item_number)].equipment_category:
                # Append item from equip_ca to game_inventory
                game_inventory.append(equip_ca[equip_ca.index(item)])
                del equip_ca[equip_ca.index(item)]
                equip_ca.append(game_inventory(int(item_number)))
                del game_inventory[int(item_number)]
            else:
                equip_ca.append(game_inventory(int(item_number)))
                del game_inventory[int(item_number)]
    else:    
        equip_ca.append(game_inventory[int(item_number)])
        del game_inventory[int(item_number)]

# disarm equipment
def disarm(player, item_number):
    pass

# disassemble equipment or Potion
def disassemble(player, item_number):
    pass

# drink potions
def drink(player, item_number):
    player.drink(item_number)
    if game_inventory[int(item_number)].number > 1:
        game_inventory[int(item_number)].number_counter_minus()
    else:
        del game_inventory[int(item_number)]

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
    "details": details
    }
