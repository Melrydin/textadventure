# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:13:26 2020

@author: Clemens
"""
import random
 
first_name_list = []
last_name_list = []
titel_list = []

# Convert First name.txxt in a list
def first_name():
    first_name = open("First name.txt","r")
    for zeile in first_name:
        if "\n" in zeile:
            zeile = zeile[:-1]
        first_name_list.append(zeile)
    first_name.close()

# Convert Last name.txt in a list
def last_name():
    last_name = open("Last name.txt","r")
    for zeile in last_name:
        if "\n" in zeile:
            zeile = zeile[:-1]
        last_name_list.append(zeile)
    last_name.close()

# Convert Titel.txt in a list
def titel():
    titel = open("Title.txt","r")
    for zeile in titel:
        if "\n" in zeile:
            zeile = zeile[:-1]
        titel_list.append(zeile)
    titel.close()

# Random name output
def enemies_name_generator():
    name_composition = random.randint(0,1)
    if name_composition == 0:
        return str(first_name_list[random.randint(0,len(first_name_list))]+ " " + last_name_list[random.randint(0, len(last_name_list))])
    else:
        return str(first_name_list[random.randint(0,len(first_name_list))]+ " " + titel_list[random.randint(0, len(titel_list))])
    
    
if __name__ == "__main__":
    first_name()
    last_name()
    titel()