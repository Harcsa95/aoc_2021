f = open("day10_data.txt", "r")

codelines = []

errorZárójel = 3
errorSzögletes = 57
errorKapcsos = 1197
errorKacsacsőr = 25137

errorSum = 0

correctZárójel = 1
correctSzögletes = 2
correctKapcsos = 3
correctKacsacsőr = 4


def bracketPairs(char):
    if(char == ')'):
        return '('
    if(char == ']'):
        return '['
    if(char == '}'):
        return '{'
    if(char == '>'):
        return '<'

def bracketClosingPairs(char):
    if(char == '('):
        return ')'
    if(char == '['):
        return ']'
    if(char == '{'):
        return '}'
    if(char == '<'):
        return '>'

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])
    

for line in f:
    line = line.strip()
    currentLine = []
    errorHappened = False
    for char in line:
        if(char == '(' or char == '[' or char == '{' or char == '<'):
            currentLine.append(char)
        else:
            if(bracketPairs(char) != currentLine[len(currentLine) - 1]):
                if(char == ')'):
                    errorSum += errorZárójel
                    errorHappened = True
                    break
                if(char == ']'):
                    errorSum += errorSzögletes
                    errorHappened = True
                    break
                if(char == '}'):
                    errorSum += errorKapcsos
                    errorHappened = True
                    break
                if(char == '>'):
                    errorSum += errorKacsacsőr
                    errorHappened = True
                    break
            else:
                currentLine.pop()
    if(not errorHappened):
        codelines.append(currentLine)

correctionList = []
for line in codelines:
    correctSum = 0
    correctionString = []
    for char in reversed(line):
        currentCompletion = bracketClosingPairs(char)
        if(currentCompletion == ')'):
            print(correctSum)
            correctSum = correctSum * 5
            correctSum += correctZárójel
            correctionString.append(currentCompletion)
        if(currentCompletion == ']'):
            print(correctSum)
            correctSum = correctSum * 5
            correctSum += correctSzögletes
            correctionString.append(currentCompletion)
        if(currentCompletion == '}'):
            print(correctSum)
            correctSum = correctSum * 5
            correctSum += correctKapcsos
            correctionString.append(currentCompletion)
        if(currentCompletion == '>'):
            print(correctSum)
            correctSum = correctSum * 5
            correctSum += correctKacsacsőr
            correctionString.append(currentCompletion)
    print(str(line))
    print(correctionString)
    correctionList.append(correctSum)
print(findMiddle(sorted(correctionList)))