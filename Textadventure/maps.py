# -*- coding: utf-8 -*-

import random

from enemies import enemie_list


class field:
    def __init__(self, enemies):
        self.enemies = enemies

    def print_state(self):
        print("Du siehst dich um und endeckst")
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(1, 3)
        erand = random.randint
        if rand == 0:
            return field([])
        elif rand == 1:
            return field([enemie_list[erand(0, len(enemie_list) - 1)]])
        elif rand == 2:
            return field([enemie_list[erand(0, len(enemie_list) - 1)], enemie_list[erand(0, len(enemie_list) - 1)]])
        elif rand == 3:
            return field([enemie_list[erand(0, len(enemie_list) - 1)], enemie_list[erand(0, len(enemie_list) - 1)], enemie_list[erand(0, len(enemie_list) - 1)]])

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x_achse = 0
        self.y_achse = 0
        for width_x in range(width):
            fields = []
            for height_y in range(height):
                fields.append(field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x_achse][self.y_achse].print_state()

    def forward(self):
        if self.x_achse == len(self.state) - 1:
            print("Du siehst hohe Berge und kommst nicht weiter")
        else:
            self.x_achse = self.x_achse + 1

    def backwards(self):
        if self.x_achse == 0:
            print("Du siehst Meer und kommst nicht wieter")
        else:
            self.x_achse = self.x_achse + 1

    def right(self):
        if self.y_achse == len(self.state[self.x_achse]) - 1:
            print("Du siehst hohe Berge und kommst nicht weiter")
        else:
            self.y_achse = self.y_achse + 1

    def left(self):
        if self.y_achse == 0:
            print("Du siehst Meer und kommst nicht wieter")
        else:
            self.y_achse = self.y_achse + 1

    def get_enemies(self):
        return self.state[self.x_achse][self.y_achse].enemies
