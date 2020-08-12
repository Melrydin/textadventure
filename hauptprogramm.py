# -*- coding: utf-8 -*-
import maps
import sys
import enemies
import Items


game_inventory = []

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

# pick up items and stow them in your inventory
def pickup(p, m):
    for i in range(len(Items.drop_list)):    
        game_inventory.append(Items.drop_list[i])
        print(game_inventory)
    Items.drop_list.clear()
    
# fight with Enemies
def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("Du wurdest verwundet und hast noch " + str(p.hp) + " HP")
        Items.loot()

# regenerate HP
def rest(p, m):
    p.rest()

# run away
def run_away(p, m):
    pass

# list all Commands
def print_help(p, m):
    for i in Commands:
        print(i)

# look in your inventory
def inventory(p, m):
    for i in game_inventory:
        print(i)
        
# Player Commands
Commands = {
    "hilfe": print_help,
    "quit": quit_game,
    "pickup": pickup,
    "forward": forward,
    "right": right,
    "left": left,
    "backwards": backwards,
    "fight": fight,
    "save": save,
    "load": load,
    "rest": rest,
    "run": run_away,
    "inventory": inventory
    }

# game loop
if __name__ == "__main__":
    name = input("Wie heißt du? ")
    p = enemies.player(name, 500, 50)
    maps = maps.Map(5,5)
    print("gib \"hilfe\" ein um eine übersicht der Befehle zu erhalten.\n")
    while True:
        command = input(">>>").lower().split(" ")
        if command[0] in Commands:
            if len(command) > 1:
                Commands[command[0]](p, maps, command[1:])
            else:
                Commands[command[0]](p, maps)
        elif command[0] not in Commands:
            print("Du rennst im Keis und tuhst garnichts.")
        if len(Items.drop_list) > 0:
            print("Du durchsuchst die Leichen und findest")
            for i in Items.drop_list:
                print(i)
        else:
            maps.print_state()
            Items.drop_list.clear()