# -*- coding: utf-8 -*-

import sys

import enemies
import inventory
import maps
from items.items import drop_list, loot


# go to the next field forward
def forward(player, maps):
    maps.forward()

# go to the next field right
def right(player, maps):
    maps.right()

# go to the next field left
def left(player, maps):
    maps.left()

# go to the next field backwards
def backwards(player, maps):
    maps.backwards()

# save your current game
def save():
    pass

# load old game
def load():
    pass

# exit game
def quit_game(player, maps):
    print("Du begehst Selbstmord und verlaesst diese Welt")
    sys.exit(0)

# fight with Enemies
def fight(player, maps):
    enemies = maps.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(player.attack)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
            loot()
        for enemie in enemies:
            player.get_hit(enemie.attack)
        print("Du wurdest verwundet und hast noch " + str(player.hp) + " HP")

# regenerate HP
def rest(player, maps):
    if len(maps.get_enemies()) == 0:
        player.rest()
        print("Du hast nun wieder " + str(int(player.hp)) + " HP")
    else:
        print("Du kannst dich im Kampf nicht ausruhen")

# run away
def run_away(player, maps):
    pass

# list all Commands
def print_help(player, maps):
    for command in Commands:
        print(command)
        
def clear(command):
    if len(drop_list) > 1 and command not in ["pickup", "fight"]:
        drop_list.clear()

# Player Commands
Commands = {
    "hilfe": print_help,
    "quit": quit_game,
    "pickup": inventory.pickup,
    "forward": forward,
    "right": right,
    "left": left,
    "backwards": backwards,
    "fight": fight,
    "save": save,
    "load": load,
    "rest": rest,
    "run": run_away,
    "inventory": inventory.inventory
    }

Commands_not_print_state = ["hilfe", "pickup", "fight",
                            "save", "load", "rest", 
                            "inventory"]

# game loop
if __name__ == "__main__":
    # Player Name
    name = input("Wie heißt du? ")
    # Player start stats
    player = enemies.player(name, 1, 500, 50, 100, 100)
    # generate Map
    maps = maps.Map(10, 10)
    print("Gib \"hilfe\" ein um eine uebersicht der Befehle zu erhalten.\n")
    while True:
        command = input(">>>").lower().split(" ")
        if command[0] in Commands:
            if len(command) > 1:
                Commands[command[0]](player, maps, command[1:])
                clear(command[0])
            else:
                Commands[command[0]](player, maps)
                clear(command[0])
        # Intercept wrong input
        elif command[0] not in Commands:
            print("Du rennst im Keis und tuhst garnichts.")
        if command[0] not in Commands:
            pass
        # show Item drops
        elif len(drop_list) > 0:
            print("Du durchsuchst die Leichen und findest")
            # print drop names
            for item in drop_list:
                print(item.name)
        elif command[0] not in Commands_not_print_state:
            maps.print_state()