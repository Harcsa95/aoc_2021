f = open("day6_data.txt", "r")

initialstates = f.readline()

lanterns = []

initialstates = initialstates.strip().split(",")
lanterns = [0]*9
for state in initialstates:
    lanterns[int(state)] += 1

new_lanterns = 0

for day in range(0,256):
    lanterns_old = lanterns.copy()
    lanterns[8] = lanterns_old[0]
    lanterns[6] = lanterns_old[0] + lanterns_old[7]
    lanterns[0] =  lanterns_old[1]
    lanterns[1] = lanterns_old[2]
    lanterns[2] = lanterns_old[3]
    lanterns[3] = lanterns_old[4]
    lanterns[4] = lanterns_old[5]
    lanterns[5] = lanterns_old[6]
    lanterns[7] = lanterns_old[8]

sum = 0
for lantern in lanterns:
    sum += lantern
print(sum)