f = open("day2_testdata.txt", "r")
aim = 0
depth = 0
horizontal = 0
for line in f:
    line2 = line.strip()
    line2 = line2.split(';')
    if (line2[0] == "forward"):
        horizontal += int(line2[1])
        print("horizontal: " + str(horizontal))
        depth += int(line2[1]) * aim
        print("depth: " + str(depth))
    if (line2[0] == "up"):
        aim -= int(line2[1])
        print("aim: " + str(aim))
    if (line2[0] == "down"):
        aim += int(line2[1])
        print("aim: " + str(aim))