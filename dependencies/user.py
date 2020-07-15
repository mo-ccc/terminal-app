import dependencies.fetch as fetch
import os.path
import time

inventory = []

def userinput(mapname):
    if os.path.exists("./sav/key.json") and "key" not in inventory:
        inventory.append("key")
    elif os.path.exists("./sav/key.json") == False and "key" in inventory:
        inventory.remove("key")
    if mapname == "./sav/main.txt":
        fetch.fromcoord(fetch.searchcharacter(mapname)[0], fetch.searchcharacter(mapname)[1])
    else:
        rows = fetch.getmap("./sav/cave.txt")
        for line in rows:
            print(line[:len(line)-1])

    entry = input("""enter 'h' to bring up help
input: """)
    entry = entry.split()
    if len(entry) < 1:
        entry.append(1)
    if len(entry) < 2:
        entry.append(1)

    for _ in range(int(entry[1])):
        rows = fetch.getmap(mapname)
        y = fetch.searchcharacter(mapname)[0]
        x = fetch.searchcharacter(mapname)[1]
        newrow = ""

        if entry[0] == "right":
            if rows[y][x + 1] == ".":
                rows[y] = rows[y].replace("*", ".")
                newrow += rows[y][:x+1] + "*" + rows[y][x+2:]
                rows[y] = newrow
                fetch.writetomap(mapname, rows)
            else:
                break

        elif entry[0] == "left":
            if rows[y][x - 1] == ".":
                rows[y] = rows[y].replace("*", ".")
                newrow += rows[y][:x-1] + "*" + rows[y][x:]
                rows[y] = newrow
                fetch.writetomap(mapname, rows)
            else:
                break

        elif entry[0] == "down":
            if rows[y + 1][x] == ".":
                rows[y] = rows[y].replace("*", ".")
                newrow += rows[y+1][:x] + "*" + rows[y+1][x+1:]
                rows[y+1] = newrow
                fetch.writetomap(mapname, rows)
            elif rows[y+1][x] == "~":
                return 1
            else:
                break

        elif entry[0] == "up":
            if rows[y - 1][x] == ".":
                rows[y] = rows[y].replace("*", ".")
                newrow += rows[y-1][:x] + "*" + rows[y-1][x+1:]
                rows[y-1] = newrow
                fetch.writetomap(mapname, rows)
            elif rows[y-1][x] == "~":
                return 1
            else:
                break
        elif entry[0] == "inventory":
            print(inventory)
            break
        elif entry[0] == "interact":
            adjacents = fetch.getadjacents(mapname)
            if "k" in adjacents:
                rows[y] = rows[y].replace("k", ".")
                key = open("./sav/key.json", "w")
                print("key obtained")
                fetch.writetomap(mapname, rows)
            if ("0" in adjacents) and (os.path.exists("./sav/key.json") == True):
                print("you win. thanks for playing")
                print("\a")
                time.sleep(1)
                return 0
            elif ("0" in adjacents) and (os.path.exists("./sav/key.json") == False):
                print("looks like some kind of key goes in here")
            break
        elif entry[0] == "quit":
            return 0
        else:
            return
