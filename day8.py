f = open("day8_testdata.txt", "r")
inputList = []
outputList = []
inOutputList = []

countUniqueDigits = 0

orig0 = "abcefg"
orig1 = "cf"
orig2 = "acdeg"
orig3 = "acdfg"
orig4 = "bcdf"
orig5 = "abdfg"
orig6 = "abdefg"
orig7 = "acf"
orig8 = "abcdefg"
orig9 = "abcdfg"


for line in f:
    line = line.strip().split(" | ")
    inputList.append(line[0].split(" "))
    outputList.append(line[1].split(" "))

inOutputList = inputList + outputList

def reduceList(digit, candidateList):
    reducedCandidateList = []
    for candidate in candidateList:
        if(candidate in digit):
            reducedCandidateList.append(candidate)
    return reducedCandidateList

def appendCandidates(digit):
    candidateList = []
    for char in digit:
        candidateList.append(char)
    return candidateList

def calculateCandidate(digit, candidateList):
    if(len(candidateList) == 0):
        return appendCandidates(digit)
    else:
        return reduceList(digit, candidateList)

for inOutput in inOutputList:
    candidateA = []
    candidateB = []
    candidateC = []
    candidateD = []
    candidateE = []
    candidateF = []
    candidateG = []

    for digit in inOutput:
        if(len(digit) == 2):
            candidateC = calculateCandidate(digit, candidateC)
            candidateF = calculateCandidate(digit, candidateF)
        if(len(digit) == 4):
            candidateB = calculateCandidate(digit, candidateB)
            candidateC = calculateCandidate(digit, candidateC)
            candidateD = calculateCandidate(digit, candidateD)
            candidateF = calculateCandidate(digit, candidateF)
        if(len(digit) == 3):
            candidateA = calculateCandidate(digit, candidateA)
            candidateC = calculateCandidate(digit, candidateC)
            candidateF = calculateCandidate(digit, candidateF)
        if(len(digit) == 7):
            candidateA = calculateCandidate(digit, candidateA)
            candidateB = calculateCandidate(digit, candidateB)
            candidateC = calculateCandidate(digit, candidateC)
            candidateD = calculateCandidate(digit, candidateD)
            candidateE = calculateCandidate(digit, candidateE)
            candidateF = calculateCandidate(digit, candidateF)
            candidateG = calculateCandidate(digit, candidateG)
        if(len(digit) == 6):
            #it can be 0,6,9
            print("gecc")

    print(candidateA)
    print(candidateB)
    print(candidateC)
    print(candidateD)
    print(candidateE)
    print(candidateF)
    print(candidateG)