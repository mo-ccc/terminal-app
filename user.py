import fetch

def charactermove(direction="right"):
    rows = fetch.getmap()
    x = fetch.searchcharacter(fetch.getmap())[0]
    y = fetch.searchcharacter(fetch.getmap())[1]
    newrow = ""
    if direction == "right":
        if rows[x][y + 1] == ".":
            rows[x] = rows[x].replace("*", ".")
            newrow += rows[x][:y+1] + "*" + rows[x][y+2:]
            rows[x] = newrow
            fetch.writetomap(rows)
    elif direction == "left":
        if rows[x][y - 1] == ".":
            rows[x] = rows[x].replace("*", ".")
            newrow += rows[x][:y-1] + "*" + rows[x][y:]
            rows[x] = newrow
            fetch.writetomap(rows)
    fetch.fromcoord(fetch.getmap(), fetch.searchcharacter(fetch.getmap())[0], fetch.searchcharacter(fetch.getmap())[1])
