import fetch

def userinput(entry="right"):
    rows = fetch.getmap()
    y = fetch.searchcharacter()[0]
    x = fetch.searchcharacter()[1]
    newrow = ""
    if entry == "right":
        if rows[y][x + 1] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y][:x+1] + "*" + rows[y][x+2:]
            rows[y] = newrow
            fetch.writetomap(rows)
    elif entry == "left":
        if rows[y][x - 1] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y][:x-1] + "*" + rows[y][x:]
            rows[y] = newrow
            fetch.writetomap(rows)
    elif entry == "down":
        if rows[y + 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y+1][:x] + "*" + rows[y+1][x+1:]
            rows[y+1] = newrow
            fetch.writetomap(rows)
    elif entry == "up":
        if rows[y - 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y-1][:x] + "*" + rows[y-1][x+1:]
            rows[y-1] = newrow
            fetch.writetomap(rows)
    elif entry == "interact":
        fetch.getadjacents()
    else:
        return
    fetch.fromcoord(fetch.searchcharacter()[0], fetch.searchcharacter()[1])
