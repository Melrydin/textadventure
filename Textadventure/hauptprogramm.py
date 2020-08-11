# -*- coding: utf-8 -*-
import maps
import sys
import enemies
import Items
    
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
    pass

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("Du wurdest verwundet und hast noch " + str(p.hp) + " HP")

def rest(p, m):
    p.rest()

def run_away(p, m):
    pass
    
def print_help(p, m):
    for i in Commands:
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
    "run": run_away
    }

if __name__ == "__main__":
    name = input("Wie heißt du? ")
    p = enemies.player(name, 1000, 100)
    maps = maps.Map(5,5)
    print("gib \"hilfe\" ein um eine übersicht der Befehle zu erhalten.\n")
    while True:
        command = input(">").lower().split(" ")
        if command[0] in Commands:
            if len(command) > 1:
                Commands[command[0]](p, maps, command[1:])
            else:
                Commands[command[0]](p, maps)
        else:
            print("Du rennst im Keis und tuhst garnichts.")
        maps.print_state()