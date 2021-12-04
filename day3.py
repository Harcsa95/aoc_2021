f = open("day3_data.txt", "r")
firstBit0 = 0
gamma_rate = [0,0,0,0,0,0,0,0,0,0,0,0]

pop_list = []
most_popular = 0
for line in f:
    line = line.strip()
    pop_list.append(line)
pop_list2 = []
for x in range(0,12):
    print(pop_list)
    for element in pop_list:
        if(int(element[x]) == 1):
            most_popular +=1
        else:
            most_popular -= 1
    if(most_popular >= 0):
        most_popular = 0
    else:
        most_popular = 1
    for element in pop_list:
        if(int(element[x]) == most_popular):
            pop_list2.append(element)
    most_popular = 0
    print(pop_list2)
    pop_list = pop_list2.copy()
    pop_list2.clear()

