import fetch

mapname = "map.txt"

def userinput(mapname):
    rows = fetch.getmap(mapname)
    y = fetch.searchcharacter(mapname)[0]
    x = fetch.searchcharacter(mapname)[1]
    newrow = ""
    if mapname == "map.txt":
        fetch.fromcoord(fetch.searchcharacter(mapname)[0], fetch.searchcharacter(mapname)[1])
    else:
        for line in rows:
            print(line[:len(line)-1])
    entry = input("""'h' to bring up help file
input: """)
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
        if rows[y+1][x] == "~":
            return 1
    elif entry == "up":
        if rows[y - 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y-1][:x] + "*" + rows[y-1][x+1:]
            rows[y-1] = newrow
            fetch.writetomap(mapname, rows)
        if rows[y-1][x] == "~":
            return 1
    elif entry == "interact":
        fetch.getadjacents(mapname)
    elif entry == "quit":
        return 0
    else:
        return
