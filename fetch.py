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

def fromcoord(rows, row, column):
    multiline = """"""
    hslice1 = column - 10
    hslice2 = column + 11
    vslice1 = row - 3
    vslice2 = row + 4
    for x in range(vslice1, vslice2):
        print(rows[x][hslice1:hslice2])

def searchcharacter(rows):
    for x in range(0,len(rows)):
        try:
            return x, rows[x].index("*")
        except:
            continue
