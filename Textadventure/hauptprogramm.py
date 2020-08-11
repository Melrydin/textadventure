# -*- coding: utf-8 -*-
import maps
import sys
import enemies
import Items
import random

drop_list = []
game_inventory = []
    
def forward(p, m):
    m.forward()
    
def right(p, m):
    m.right()
    
def left(p, m):
    m.left()
    
def backwards(p, m):
    m.backwards()
    
def save():
    pass

def load():
    pass

def quit_game(p, m):
    print("Du begehst Selbstmord und verlaesst diese Welt")
    sys.exit(0)

def pickup(p, m):
    game_inventory.append(drop_list[0])
    drop_list.clear()
    

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("Du wurdest verwundet und hast noch " + str(p.hp) + " HP")
    rand = random.randint(0,1)
    if rand == 1:
        item_category = Items.Item_list[random.randint(0, len(Items.Item_list) - 1)]
        item = item_category[random.randint(0, len(item_category) - 1)]
        drop_list.append(item)

def rest(p, m):
    p.rest()

def run_away(p, m):
    pass
    
def print_help(p, m):
    for i in Commands:
        print(i)

def inventory(p, m):
    for i in game_inventory:
        print(i)

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

if __name__ == "__main__":
    name = input("Wie heißt du? ")
    p = enemies.player(name, 1000, 100)
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
        if len(drop_list) > 0:
            print("Du durchsuchst die Leichen und findest")
            for i in drop_list:
                print(i)
            if command[0] != "pickup":
                drop_list.clear()
        else:
            maps.print_state()
            drop_list.clear()