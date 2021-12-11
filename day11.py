f = open("day11_data.txt", "r")

octopusEnergyLevels = []
global numberOfFlashes
numberOfFlashes = 0
for line in f:
    line = line.strip()
    rowOfOctopus = []
    for octopus in line:
        rowOfOctopus.append(int(octopus))
    octopusEnergyLevels.append(rowOfOctopus)

def increaseOctopus(currentOctopus, currentRowOfOctopus, currentColumnOfOctopus):
    if(octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus] < 9 and octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus] != -1):
        octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus] += 1
    elif(octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus] != -1):
        octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus] = -1
        global numberOfFlashes
        numberOfFlashes += 1
        if(currentRowOfOctopus+1 < 10):
            increaseOctopus(octopusEnergyLevels[currentRowOfOctopus+1][currentColumnOfOctopus], currentRowOfOctopus+1, currentColumnOfOctopus)
            if(currentColumnOfOctopus+1 < 10):
                increaseOctopus(octopusEnergyLevels[currentRowOfOctopus+1][currentColumnOfOctopus+1], currentRowOfOctopus+1, currentColumnOfOctopus+1)
            if(currentColumnOfOctopus-1 >= 0):
                increaseOctopus(octopusEnergyLevels[currentRowOfOctopus+1][currentColumnOfOctopus-1], currentRowOfOctopus+1, currentColumnOfOctopus-1)
        if(currentColumnOfOctopus-1 >= 0):
            increaseOctopus(octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus-1], currentRowOfOctopus, currentColumnOfOctopus-1)
        if(currentColumnOfOctopus+1 < 10):
            increaseOctopus(octopusEnergyLevels[currentRowOfOctopus][currentColumnOfOctopus+1], currentRowOfOctopus, currentColumnOfOctopus+1)
        if(currentRowOfOctopus-1 >= 0):
            increaseOctopus(octopusEnergyLevels[currentRowOfOctopus-1][currentColumnOfOctopus], currentRowOfOctopus-1, currentColumnOfOctopus)
            if(currentColumnOfOctopus+1 < 10):
                increaseOctopus(octopusEnergyLevels[currentRowOfOctopus-1][currentColumnOfOctopus+1], currentRowOfOctopus-1, currentColumnOfOctopus+1)
            if(currentColumnOfOctopus-1 >= 0):
                increaseOctopus(octopusEnergyLevels[currentRowOfOctopus-1][currentColumnOfOctopus-1], currentRowOfOctopus-1, currentColumnOfOctopus-1)

def initEnergyLevels():
    for rowOfOctopus in range(0, 10):
        for columnOfOctopus in range(0,10):
            currentOctopus = octopusEnergyLevels[rowOfOctopus][columnOfOctopus]
            if(currentOctopus == -1):
                octopusEnergyLevels[rowOfOctopus][columnOfOctopus] = 0
def isAllZero():
    for rowOfOctopus in range(0, 10):
        for columnOfOctopus in range(0,10):
            currentOctopus = octopusEnergyLevels[rowOfOctopus][columnOfOctopus]
            if(currentOctopus != 0):
                return False
    return True
for steps in range(0, 1000):
    initEnergyLevels()
    if(isAllZero()):
        print("gyozelem: " + str(steps))
    for rowOfOctopus in range(0, 10):
        for columnOfOctopus in range(0,10):
            currentOctopus = octopusEnergyLevels[rowOfOctopus][columnOfOctopus]
            increaseOctopus(currentOctopus, rowOfOctopus, columnOfOctopus)
print(numberOfFlashes)
            

                
                
