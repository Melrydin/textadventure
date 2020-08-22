# -*- coding: utf-8 -*-

import maps
import sys
import enemies
import inventory
from items.items import loot, drop_list

# go to the next field forward  
def forward(p, m):
    m.forward()

# go to the next field right
def right(p, m):
    m.right()

# go to the next field left    
def left(p, m):
    m.left()

# go to the next field backwards  
def backwards(p, m):
    m.backwards()

# save your current game
def save():
    pass

# load old game
def load():
    pass

# exit game
def quit_game(p, m):
    print("Du begehst Selbstmord und verlaesst diese Welt")
    sys.exit(0)
    
# fight with Enemies
def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.attack)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
            loot()
        for i in enemies:
            p.get_hit(i.attack)
        print("Du wurdest verwundet und hast noch " + str(p.hp) + " HP")

# regenerate HP
def rest(p, m):
    if len(m.get_enemies()) == 0:
        p.rest()
        print("Du hast nun wieder " + str(int(p.hp)) + " HP")
    else:
        print("Du kannst dich im Kampf nicht ausruhen")

# run away
def run_away(p, m):
    pass

# list all Commands
def print_help(p, m):
    for i in Commands:
        print(i)
        
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

Commands_not_print_state = ["hilfe", "pickup", "fight", "save", "load", "rest", "inventory"]

# game loop
if __name__ == "__main__":
    # Player Name
    name = input("Wie heißt du? ")
    # Player start stats
    p = enemies.player(name, 500, 1, 50, 100, 100)
    # generate Map
    maps = maps.Map(10,10)
    print("Gib \"hilfe\" ein um eine uebersicht der Befehle zu erhalten.\n")
    while True:
        command = input(">>>").lower().split(" ")
        if command[0] in Commands:
            if len(command) > 1:
                Commands[command[0]](p, maps, command[1:])
            else:
                Commands[command[0]](p, maps)
        # Intercept wrong input
        elif command[0] not in Commands:
            print("Du rennst im Keis und tuhst garnichts.")
        if command[0] not in Commands:
            pass
        # show Item drops
        elif len(drop_list) > 0:
            print("Du durchsuchst die Leichen und findest")
            # print drop mames
            for i in drop_list:
                print(i.name)
        elif command[0] not in Commands_not_print_state:
            maps.print_state()
        else:
            drop_list.clear()