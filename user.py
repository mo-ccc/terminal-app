import fetch

def charactermove(direction="right"):
    rows = fetch.getmap()
    y = fetch.searchcharacter(fetch.getmap())[0]
    x = fetch.searchcharacter(fetch.getmap())[1]
    newrow = ""
    if direction == "right":
        if rows[y][x + 1] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y][:x+1] + "*" + rows[y][x+2:]
            rows[y] = newrow
            fetch.writetomap(rows)
    elif direction == "left":
        if rows[y][x - 1] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y][:x-1] + "*" + rows[y][x:]
            rows[y] = newrow
            fetch.writetomap(rows)
    elif direction == "down":
        if rows[y + 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y+1][:x] + "*" + rows[y+1][x+1:]
            rows[y+1] = newrow
            fetch.writetomap(rows)
    elif direction == "up":
        if rows[y - 1][x] == ".":
            rows[y] = rows[y].replace("*", ".")
            newrow += rows[y-1][:x] + "*" + rows[y-1][x+1:]
            rows[y-1] = newrow
            fetch.writetomap(rows)
    fetch.fromcoord(fetch.getmap(), fetch.searchcharacter(fetch.getmap())[0], fetch.searchcharacter(fetch.getmap())[1])
