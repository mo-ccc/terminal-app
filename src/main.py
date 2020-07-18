#!/usr/sbin/python

import dependencies.user as user
import dependencies.initialise as initialise
import dependencies.fetch as fetch
import os.path
import time
import json

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

# Checks to see if save data is present and if not creates it
if os.path.isdir("sav") == False:
    time.sleep(1)
    print("no save data found. creating...")
    os.mkdir("sav")
if os.path.exists("sav/cave.txt") == False:
    initialise.create_cave()
if os.path.exists("sav/main.txt") == False:
    initialise.create_main()
    if os.path.exists("sav/key.json") == True:
        os.remove("sav/savedata.json")
if os.path.exists("sav/savedata.json") == False:
    initialise.create_save()
if os.path.exists("help.txt") == False:
    initialise.create_helpfile()

time.sleep(1)
print("welcome to the game")
time.sleep(1)

while True:
    #open save file and load it into current map variable
    sr = open("sav/savedata.json", "r")
    jreadsave = sr.read()
    sr.close()
    readsave = json.loads(jreadsave)
    current_map = readsave["current_map"]

    #running user input function
    mainexecution = user.userinput(current_map)  
    #if 1 is returned switch map
    if mainexecution == 1:
        if current_map == "sav/main.txt":
            diction = {"current_map":"sav/cave.txt"}
            sw = open("sav/savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
        elif current_map == "sav/cave.txt":
            diction = {"current_map":"sav/main.txt"}
            sw = open("sav/savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
    #if 0 is returned exit
    elif mainexecution == 0:
        print("goodbye")
        break
        

    
