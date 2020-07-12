def getmap():
    mapf = open("map.txt", "r")
    rows = []
    for x in mapf:
        rows.append(x)
    return rows

def writetomap(rows):
    mapf = open("map.txt", "w")
    for x in rows:
        mapf.write(x)
    mapf.close()

def fromcoord(row, column):
    rows = getmap()
    multiline = """"""
    hslice1 = column - 10
    hslice2 = column + 11
    vslice1 = row - 3
    vslice2 = row + 4
    for x in range(vslice1, vslice2):
        print(rows[x][hslice1:hslice2])

def searchcharacter():
    rows = getmap()
    for x in range(0,len(rows)):
        try:
            return x, rows[x].index("*")
        except:
            continue

def getadjacents():
    x = searchcharacter()[1]
    y = searchcharacter()[0]
    rows = getmap()
    adjacents = []
    possiblex = [x-1, x, x+1]
    possibley = [y-1, y, y+1]
    for a in possibley:
        for b in possiblex:
            adjacents.append(rows[a][b])
    print(f"here are adjacents: {adjacents}")




