# Read Input File
inputFile = open('input/day1_input.txt', 'r')
lines = inputFile.readlines()

# Variables
sumFoodItemCalories = 0
count = 0
sumElfCaloriesList = []
topThreeElfCaloriesTotal = 0

# For each line in the text file...
for line in lines:
    if line.strip() != "":  # ... if line is not blank
        sumFoodItemCalories = sumFoodItemCalories + int(line.strip())  # add that elf's food item calories to
    else:
        sumElfCaloriesList.append(sumFoodItemCalories)  # add the sumFoodItemCalories for a given Elf to a list
        sumFoodItemCalories = 0   # reset sumCalories to 0

# Find the Elf with the most total calories
sumElfCaloriesList.sort()
print("Total calories that the top elf is carrying is {} calories.".format(sumElfCaloriesList[-1]))
print()

# Sum of the top 3 Elves with the most total calories
topThreeElfCaloriesTotal = sum(sumElfCaloriesList[-3:])
print("Total calories top 3 elves are carrying is {} calories.".format(topThreeElfCaloriesTotal))
