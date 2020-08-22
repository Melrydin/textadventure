# -*- coding: utf-8 -*-
from items.items import drop_list


game_inventory = []

armor_list = []
non_armor_list = []
weapon_list = []

equip_list = [armor_list,non_armor_list,weapon_list]

# pick up items and stow them in your inventory
def pickup(p, m):
    for i in range(len(drop_list)):
        # stacking double Items
        if drop_list[i] in game_inventory:
            game_inventory[game_inventory.index(drop_list[i])].number_counter_plus()
        else:
            # append new Item
            game_inventory.append(drop_list[i])
    drop_list.clear()


# look in your inventory
def inventory(p, m):
    print("Gib \"hilfe\" ein um eine uebersicht der Inventar Befehle zu erhalten.\n")
    print(6* "-" + "Inventory" + 6* "-")
    for i in range(len(game_inventory)):
        print(str(i+1) + ": " + str(game_inventory[i].number) + "x" + game_inventory[i].name)
        inventory_Commands.update({str(i):i})
    while True:
        inventory_command = input("Inventory >>>").lower().split(" ")
        if inventory_command[0] in inventory_Commands:
            if len(inventory_command) > 1:
                inventory_Commands[inventory_command[1]](p, inventory_command[0])
            else:
                inventory_Commands[inventory_command[0]]()
        elif inventory_command[0] == "quit":
            break
        else:
            print("Was tuhst du da? Du wuehlst Sinnlos in deiner Tasche.")
        print("")
        print(6* "-" + "Inventory" + 6* "-")
        for i in range(len(game_inventory)):
            print(str(i+1) + ": " + str(game_inventory[i].number) + "x" + game_inventory[i].name)
    for i in range(len(game_inventory)):
        inventory_Commands.pop(str(i), None)

# equip equipment
def equip(item_number):
    pass

# disarm equipment
def disarm(item_number):
    pass

# disassemble equipment or Potion
def disassemble(item_number):
    pass

def drink(p, item_number):
    p.drink(item_number)

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
    "disassemble": disassemble
    }

