# Read Input File
inputFile = open('input/day2_Input.txt', 'r')
lines = inputFile.readlines()

# Variables
totalScore = 0

# Part 1
# For each line in the text file...

for game in lines:
    if game[0] == 'A':
        if game[2] == 'X':
            totalScore += 4
        elif game[2] == 'Y':
            totalScore += 8
        elif game[2] == 'Z':
            totalScore += 3
    elif game[0] == 'B':
        if game[2] == 'X':
            totalScore += 1
        elif game[2] == 'Y':
            totalScore += 5
        elif game[2] == 'Z':
            totalScore += 9
    elif game[0] == 'C':
        if game[2] == 'X':
            totalScore += 7
        elif game[2] == 'Y':
            totalScore += 2
        elif game[2] == 'Z':
            totalScore += 6
    else:
        print("Invalid category")

print(totalScore)

totalScore = 0

for game in lines:
    if game[0] == 'A':
        if game[2] == 'X':
            totalScore += 3
        elif game[2] == 'Y':
            totalScore += 4
        elif game[2] == 'Z':
            totalScore += 8
    elif game[0] == 'B':
        if game[2] == 'X':
            totalScore += 1
        elif game[2] == 'Y':
            totalScore += 5
        elif game[2] == 'Z':
            totalScore += 9
    elif game[0] == 'C':
        if game[2] == 'X':
            totalScore += 2
        elif game[2] == 'Y':
            totalScore += 6
        elif game[2] == 'Z':
            totalScore += 7
    else:
        print("Invalid category")

print(totalScore)
