#!/usr/sbin/python

import dependencies.user as user
import dependencies.initialise as initialise
import dependencies.fetch as fetch
import os.path
import time
import json
import sys
import shutil

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

#help sys argument
if "--help" in sys.argv:
    print("""
    - To run the game simply run it without the --help argument. It will handle initialisation on its own.
    - If u wish to delete all save data without affecting the application use the "--clear" flag.
    - To get a list of all flags use "--listargs"
    """)

#clear sys argument removes all save data
elif "--clear" in sys.argv:
    if os.path.isdir("sav") == True:
        shutil.rmtree("sav")
    if os.path.exists("help.txt"):
        os.remove("help.txt")

elif "--all" in sys.argv:
    print(sys.argv)

elif "--listargs" in sys.argv:
    print(["--help", "--clear", "--all", "--listargs"])

#main application
else:
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
            os.remove("sav/key.json")
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
        
