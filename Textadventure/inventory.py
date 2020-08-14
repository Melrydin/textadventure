# -*- coding: utf-8 -*-
import items

game_inventory = []

armor_list = []
non_armor_list = []
weapon_list = []

equip_list = [armor_list,non_armor_list,weapon_list]

# pick up items and stow them in your inventory
def pickup(p, m):
    for i in range(len(items.drop_list)):    
        game_inventory.append(items.drop_list[i])
    items.drop_list.clear()


# look in your inventory
def inventory(p, m):
    print("Gib \"hilfe\" ein um eine uebersicht der Inventar Befehle zu erhalten.\n")
    print(6* "-" + "Inventory" + 6* "-")
    for i in range(len(game_inventory)):
        print(str(i+1) + ": " + game_inventory[i].name)
        inventory_Commands.update({str(i):i})
    while True:
        inventory_command = input("Inventory >>>").lower().split(" ")
        if inventory_command[0] in inventory_Commands:
            if len(inventory_command) > 1:
                inventory_Commands[inventory_command[1]](inventory_command[0])
            else:
                inventory_Commands[inventory_command[0]]()
        elif inventory_command[0] == "exit_inventory":
            break
        else:
            print("Was tuhst du da? Du wuehlst Sinnlos in deiner Tasche.")
    for i in range(len(game_inventory)):
        inventory_Commands.pop(str(i), None)

# equip equipment
def equip(item_number):
    pass

# disarm equipment
def disarm(item_number):
    pass

# drink Potion
def drink(item_number):
    pass

# disassemble equipment or Potion
def disassemble(item_number):
    pass

# print invrntory Commsnds
def print_help():
    for i in inventory_Commands:
        print(i)

# Player inventory Commands
inventory_Commands = {
    "hilfe": print_help,
    "equip": equip,
    "disarm": disarm,
    "drink": drink,
    "disassemble": disassemble
    }

