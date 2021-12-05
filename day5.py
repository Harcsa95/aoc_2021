f = open("day5_data.txt", "r")

num_lines = sum(1 for line in open('day5_data.txt'))

lines_at_coordinate = []
lines_at_coordinate = [ [0]*1000 for i in range(1000)]

coord_list = []

for x in range(0, num_lines):
    line = f.readline()
    line = line.strip().split("->")
    fromCoord = line[0].split(',')
    toCoord = line[1].split(',')
    lines_at_coordinate[0]
    coords = [int(fromCoord[0]), int(fromCoord[1]), int(toCoord[0]), int(toCoord[1])]
    coord_list.append(coords)

for coord in coord_list:
    if(coord[0] == coord[2]):
        fromCoord = coord[1]
        toCoord = coord[3]
        if(coord[1] > coord[3]):
            fromCoord = coord[3]
            toCoord = coord[1]
        for x in range(fromCoord, toCoord + 1):
            lines_at_coordinate[x][coord[0]] += 1
    if(coord[1] == coord[3]):
        fromCoord = coord[0]
        toCoord = coord[2]
        if(coord[0] > coord[2]):
            fromCoord = coord[2]
            toCoord = coord[0]
        for x in range(fromCoord, toCoord + 1):
            lines_at_coordinate[coord[1]][x] += 1
    if(coord[1] != coord[3] and coord[0] != coord[2]):
        fromYCoord = coord[0]
        toYCoord = coord[2]
        fromXCoord = coord[1]
        toXCoord = coord[3]
        if(coord[0] > coord[2]):
            fromYCoord = coord[2]
            toYCoord = coord[0]
            fromXCoord = coord[3]
            toXCoord = coord[1]
        for x in range(fromYCoord, toYCoord + 1):
            lines_at_coordinate[fromXCoord][x] += 1
            if(fromXCoord < toXCoord):
                fromXCoord += 1
            else:
                fromXCoord -= 1
        
largerThan2 = 0
for line in lines_at_coordinate:
    for number in line:
        if(number >= 2):
            largerThan2 += 1

print(largerThan2)
