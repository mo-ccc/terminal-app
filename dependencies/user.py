import dependencies.fetch as fetch
import os.path
import time

inventory = []

def inventorycheck():
    if os.path.exists("./sav/key.json") and "key" not in inventory:
        inventory.append("key")
    elif os.path.exists("./sav/key.json") == False and "key" in inventory:
        inventory.remove("key")

def map_print(mapname):
    if mapname == "./sav/main.txt":
        fetch.fromcoord(fetch.searchcharacter(mapname)[0], fetch.searchcharacter(mapname)[1])
    else:
        rows = fetch.getmap("./sav/cave.txt")
        for line in rows:
            print(line[:len(line)-1])

def movement(horizontal, vertical, rows, x, y, mapname):
    newrow = ""
    if rows[y + vertical][x + horizontal] == ".":
                rows[y] = rows[y].replace("*", ".")
                newrow += rows[y+vertical][:x+horizontal] + "*" + rows[y+vertical][x+1+horizontal:]
                rows[y+vertical] = newrow
                fetch.writetomap(mapname, rows)
    elif rows[y + vertical][x + horizontal] == "~":
        return 1
    else:
        return 0

def interactfunc():
    adjacents = fetch.getadjacents(mapname)
    if "k" in adjacents:
        for y in rows:
            rows[y] = rows[y].replace("k", ".")
        key = open("./sav/key.json", "w")
        print("\n********key obtained*********\n")
        fetch.writetomap(mapname, rows)
    if ("0" in adjacents) and (os.path.exists("./sav/key.json") == True):
        print("you win. thanks for playing")
        time.sleep(1)
        print("\a")
        time.sleep(1)
        return 0
    elif ("0" in adjacents) and (os.path.exists("./sav/key.json") == False):
        print("looks like some kind of key goes in here")

def userinput(mapname):
    inventorycheck()
    map_print(mapname)

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
            if movement(1, 0, rows, x, y, mapname) == 0:
                break

        elif entry[0] == "left":
            if movement(-1, 0, rows, x, y, mapname) == 0:
                break

        elif entry[0] == "down":
            d = movement(0, 1, rows, x, y, mapname)
            if d == 0:
                break
            elif d == 1:
                return 1

        elif entry[0] == "up":
            d = movement(0, -1, rows, x, y, mapname)
            if d == 0:
                break
            elif d == 1:
                return 1

        elif entry[0] == "inventory":
            print(inventory)
            break

        elif entry[0] == "interact":
            if interactfunc() == 0:
                return 0
            break

        elif entry[0] == "quit":
            return 0

        elif entry[0] == "help":
            helpfile = open("help.txt", "r")
            print(helpfile.read())
            helpfile.close()

        else:
            return
