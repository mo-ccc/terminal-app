import user
import fetch
import json

while True:
    sr = open("savedata.json", "r")
    jreadsave = sr.read()
    sr.close()
    readsave = json.loads(jreadsave)
    current_map = readsave["current_map"]
    perid = user.userinput(current_map)  
    if perid == 1:
        if current_map == "map.txt":
            diction = {"current_map":"cave.txt"}
            sw = open("savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
        elif current_map == "cave.txt":
            diction = {"current_map":"map.txt"}
            sw = open("savedata.json", "w")
            json.dump(diction, sw)
            sw.close()
    elif perid == 0:
        print("goodbye")
        break
        

    
