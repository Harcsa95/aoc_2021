f = open("day4_data.txt", "r")

firstline = f.readline()
firstline = firstline.strip()
firstline = firstline.split(',')

randomNumbers = []

class bingo:
    def __init__(self):
        self.first_row = []
        self.second_row = []
        self.third_row = []
        self.fourth_row = []
        self.fifth_row = []
        self.first_column = []
        self.second_column = []
        self.third_column = []
        self.fourth_column = []
        self.fifth_column = []
    def __str__(self):
        return f'{self.first_column}\n{self.second_column}\n{self.third_column}\n{self.fourth_column}\n{self.fifth_column}'

    def __repr__(self):
        return f'{self.first_column}\n{self.second_column}\n{self.third_column}\n{self.fourth_column}\n{self.fifth_column}'

bingo_list = []

def grouped(iterator, size):
    yield tuple(next(iterator) for _ in range(size))

for element in firstline:
    randomNumbers.append(int(element))

for lines in f:
    for line1, line2, line3, line4, line5 in grouped(f, size=5):
        bingo_board = bingo()
        line1 = line1.strip().split()
        line2 = line2.strip().split()
        line3 = line3.strip().split()
        line4 = line4.strip().split()
        line5 = line5.strip().split()

        bingo_board.first_row = line1
        bingo_board.second_row = line2
        bingo_board.third_row = line3
        bingo_board.fourth_row = line4
        bingo_board.fifth_row = line5
        
        bingo_board.first_column.append(line1[0])
        bingo_board.first_column.append(line2[0])
        bingo_board.first_column.append(line3[0])
        bingo_board.first_column.append(line4[0])
        bingo_board.first_column.append(line5[0])

        bingo_board.second_column.append(line1[1])
        bingo_board.second_column.append(line2[1])
        bingo_board.second_column.append(line3[1])
        bingo_board.second_column.append(line4[1])
        bingo_board.second_column.append(line5[1])

        bingo_board.third_column.append(line1[2])
        bingo_board.third_column.append(line2[2])
        bingo_board.third_column.append(line3[2])
        bingo_board.third_column.append(line4[2])
        bingo_board.third_column.append(line5[2])

        bingo_board.fourth_column.append(line1[3])
        bingo_board.fourth_column.append(line2[3])
        bingo_board.fourth_column.append(line3[3])
        bingo_board.fourth_column.append(line4[3])
        bingo_board.fourth_column.append(line5[3])

        bingo_board.fifth_column.append(line1[4])
        bingo_board.fifth_column.append(line2[4])
        bingo_board.fifth_column.append(line3[4])
        bingo_board.fifth_column.append(line4[4])
        bingo_board.fifth_column.append(line5[4])
        
        bingo_list.append(bingo_board)

bingo_to_remove = []
for number in randomNumbers:
    for bingoBoard in bingo_list:
        if(bingoBoard.first_row.count(str(number)) != 0):
            bingoBoard.first_row.remove(str(number))
        if(bingoBoard.second_row.count(str(number)) != 0):
            bingoBoard.second_row.remove(str(number))
        if(bingoBoard.third_row.count(str(number)) != 0):
            bingoBoard.third_row.remove(str(number))
        if(bingoBoard.fourth_row.count(str(number)) != 0):
            bingoBoard.fourth_row.remove(str(number))
        if(bingoBoard.fifth_row.count(str(number)) != 0):
            bingoBoard.fifth_row.remove(str(number))

        if(bingoBoard.first_column.count(str(number)) != 0):
            bingoBoard.first_column.remove(str(number))
        if(bingoBoard.second_column.count(str(number)) != 0):
            bingoBoard.second_column.remove(str(number))
        if(bingoBoard.third_column.count(str(number)) != 0):
            bingoBoard.third_column.remove(str(number))
        if(bingoBoard.fourth_column.count(str(number)) != 0):
            bingoBoard.fourth_column.remove(str(number))
        if(bingoBoard.fifth_column.count(str(number)) != 0):
            bingoBoard.fifth_column.remove(str(number))
        if(len(bingoBoard.first_column) == 0 or len(bingoBoard.second_column) == 0 or len(bingoBoard.third_column) == 0 or len(bingoBoard.fourth_column) == 0 or len(bingoBoard.fifth_column) == 0 or len(bingoBoard.first_row) == 0 or len(bingoBoard.second_row) == 0 or len(bingoBoard.third_row) == 0 or len(bingoBoard.fourth_row) == 0 or len(bingoBoard.fifth_row) == 0):
            sum = 0
            for numberz in bingoBoard.first_column:
                sum += int(numberz)
            for numberz in bingoBoard.second_column:
                sum += int(numberz)
            for numberz in bingoBoard.third_column:
                sum += int(numberz)
            for numberz in bingoBoard.fourth_column:
                sum += int(numberz)
            for numberz in bingoBoard.fifth_column:
                sum += int(numberz)
            print("gyozelem: " + str(number) + " sum: " + str(sum))
            bingo_to_remove.append(bingoBoard)
        else:
            print(bingoBoard)
            print("\n")
    for bingoRemove in bingo_to_remove:
        if(bingo_list.count(bingoRemove)):
            bingo_list.remove(bingoRemove)
    bingoRemove = []