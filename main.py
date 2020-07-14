import user
import fetch
import json
import os.path
import initialise

if os.path.isdir("./sav") == False:
    print("no save data found. creating...")
    os.mkdir("./sav")
if os.path.exists("./sav/cave.txt") == False:
    initialise.create_cave()
if os.path.exists("./sav/main.txt") == False:
    initialise.create_main()
if os.path.exists("./sav/savedata.json") == False:
    initialise.create_save()

while True:
    sr = open("./sav/savedata.json", "r")
    jreadsave = sr.read()
    sr.close()
    readsave = json.loads(jreadsave)
    current_map = readsave["current_map"]
    perid = user.userinput(current_map)  
    if perid == 1:
        if current_map == "map.txt":
            diction = {"current_map":"cave.txt"}
            sw = open("./sav/savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
        elif current_map == "cave.txt":
            diction = {"current_map":"map.txt"}
            sw = open("./sav/savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
    elif perid == 0:
        print("goodbye")
        break
        

    
