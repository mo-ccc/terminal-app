#places map file into list for manipulation
def getmap(mapname):
    mapf = open(mapname, "r")
    rows = []
    for x in mapf:
        rows.append(x)
    return rows

#writes list into map file
def writetomap(mapname, rows):
    mapf = open(mapname, "w")
    for x in rows:
        mapf.write(x)
    mapf.close()

#prints slice of map from coordinates
def fromcoord(row, column):
    rows = getmap("sav/main.txt")
    hslice1 = column - 15
    hslice2 = column + 16
    vslice1 = row - 4
    vslice2 = row + 5
    for x in range(vslice1, vslice2):
        print(rows[x][hslice1:hslice2])

#returns coordinates of player. exception for rows not found in.
def searchcharacter(mapname):
    rows = getmap(mapname)
    for x in range(0,len(rows)):
        try:
            return x, rows[x].index("*")
        except:
            continue

#loads values of all adjacent items into a list
def getadjacents(mapname):
    x = searchcharacter(mapname)[1]
    y = searchcharacter(mapname)[0]
    rows = getmap(mapname)
    adjacents = []
    possiblex = [x-1, x, x+1]
    possibley = [y-1, y, y+1]
    for a in possibley:
        for b in possiblex:
            adjacents.append(rows[a][b])
    return adjacents




