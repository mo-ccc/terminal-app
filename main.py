mapf = open("map.txt", "r")
line = []
for x in mapf:
    line.append(x)

def searchcharacter():
    

def fromcoord(row, column):
    hslice1 = column - 10
    hslice2 = column + 10
    vslice1 = row - 2
    vslice2 = row + 3
    for x in range(vslice1, vslice2):
        print(line[x][hslice1:hslice2])

fromcoord(4, 24)

    
