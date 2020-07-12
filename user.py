import fetch

def cave_entered(current_map):
    if (fetch.searchcharacter("map.txt") == ((8, 23) or (8, 24))) and current_map == "main":
        return True

def cave_exited(mapname):
    if (fetch.searchcharacter("cave.txt") == (9, 15)) and current_map == "cave":
        return True

def userinput(entry="right", mapname):
    rows = fetch.getmap(mapname)
    y = fetch.searchcharacter(mapname)[0]
    x = fetch.searchcharacter(mapname)[1]
    newrow = ""
    if entry == "right":
        if rows[y][x + 1] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y][:x+1] + "*" + rows[y][x+2:]
            rows[y] = newrow
            fetch.writetomap(mapname, rows)
    elif entry == "left":
        if rows[y][x - 1] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y][:x-1] + "*" + rows[y][x:]
            rows[y] = newrow
            fetch.writetomap(mapname, rows)
    elif entry == "down":
        if rows[y + 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y+1][:x] + "*" + rows[y+1][x+1:]
            rows[y+1] = newrow
            fetch.writetomap(mapname, rows)
    elif entry == "up":
        if rows[y - 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y-1][:x] + "*" + rows[y-1][x+1:]
            rows[y-1] = newrow
            fetch.writetomap(mapname, rows)
    elif entry == "interact":
        fetch.getadjacents(mapname)
    else:
        return
    if mapname == "map.txt":
        fetch.fromcoord(fetch.searchcharacter(mapname)[0], fetch.searchcharacter(mapname)[1])
    else:
        for line in mapname:
            print(line)
