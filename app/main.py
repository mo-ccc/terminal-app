import dependencies.user as user
import dependencies.initialise as initialise
import dependencies.fetch as fetch
import os.path
import time
import json

if os.path.isdir("./sav") == False:
    time.sleep(1)
    print("no save data found. creating...")
    os.mkdir("./sav")
if os.path.exists("./sav/cave.txt") == False:
    initialise.create_cave()
if os.path.exists("./sav/main.txt") == False:
    initialise.create_main()
if os.path.exists("./sav/savedata.json") == False:
    initialise.create_save()
if os.path.exists("help.txt") == False:
    initialise.create_helpfile()

time.sleep(1)
print("welcome to the game")
time.sleep(1)

while True:
    sr = open("./sav/savedata.json", "r")
    jreadsave = sr.read()
    sr.close()
    readsave = json.loads(jreadsave)
    current_map = readsave["current_map"]
    perid = user.userinput(current_map)  
    if perid == 1:
        if current_map == "./sav/main.txt":
            diction = {"current_map":"./sav/cave.txt"}
            sw = open("./sav/savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
        elif current_map == "./sav/cave.txt":
            diction = {"current_map":"./sav/main.txt"}
            sw = open("./sav/savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
    elif perid == 0:
        print("goodbye")
        break
        

    
