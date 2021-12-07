f = open("day7_data.txt", "r")

initialpositions = f.readline()

initialpositions = initialpositions.strip().split(",")
minPosition = 10000
maxPosition = 0

for position in initialpositions:
    if(int(position) < minPosition):
        minPosition = int(position)
    if(int(position) > maxPosition):
        maxPosition = int(position)

minFuel = 4000000000000
for x in range(minPosition, maxPosition):
    currentMinFuel = 0
    for position in initialpositions:
        stepsNeeded = abs(int(position) - x)
        sumOfFuel = sum(range(stepsNeeded+1))
        currentMinFuel += sumOfFuel 
    if(currentMinFuel < minFuel):
        minFuel = currentMinFuel

print(minFuel)