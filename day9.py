f = open("day9_testdata.txt", "r")

heightmap = []
for line in f:
    line = line.strip()
    rowOfHeatmap = []
    for number in line:
        rowOfHeatmap.append(int(number))
    heightmap.append(rowOfHeatmap)
sumOfRiskLevels = 0
for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        currentPoint = heightmap[y][x]
        aboveBigger = True
        belowBigger = True
        toRightBigger = True
        toLeftBigger = True

        if(x != 0):
            toLeftBigger = heightmap[y][x-1] > currentPoint
        if(x != len(heightmap[y])-1):
            toRightBigger = heightmap[y][x+1] > currentPoint
        if(y != 0):
            aboveBigger = heightmap[y-1][x] > currentPoint
        if(y != len(heightmap)-1):
            belowBigger = heightmap[y+1][x] > currentPoint
        if(toLeftBigger and toRightBigger and belowBigger and aboveBigger):
            

print(sumOfRiskLevels)