f = open("day6_data.txt", "r")

initialstates = f.readline()

initialstates = initialstates.strip().split(",")
lanterns = [0]*10
for state in initialstates:
    lanterns.append(int(state))

new_lanterns = []

for day in range(0,256):
    for current_lantern in range(0,len(lanterns)):
        if(lanterns[current_lantern] == 0):
            lanterns[current_lantern] = 6
            new_lanterns.append(8)
        else:
            lanterns[current_lantern] = lanterns[current_lantern] - 1
    lanterns.extend(new_lanterns)
    new_lanterns = []
    if(day > 100 and day%10 == 0):
        print("day: " + str(day))
print(len(lanterns))