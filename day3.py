# Day 3: Rucksack Reorganization Part 1 #

# Imports
import string

# Read Input File
inputFile = open('input/day3_input.txt', 'r')
rucksacks = inputFile.readlines()
rucksackList = []

# Variables
priorityValue = 1
prioritySumValue = 0
allElfGroups = list()
elfGroupsDictionary = {}
elfGroupPriorityValue = 0
elfGroupBadgeList = []

priority = dict.fromkeys(string.ascii_letters, 0)  # Dictionary for the priority values
for item in priority:
    priority[item] = priorityValue  # Set the priority value of each letter
    priorityValue += 1  # Increase the priority value of each letter

for rucksack in rucksacks:
    rucksackList.append(rucksack.strip())
    compartment1, compartment2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]  # Split rucksack in half
    compartments = list(set(compartment1) & set(compartment2))
    for matchingItem in compartments:
        prioritySumValue += (priority[matchingItem])

print("Sum of the priorities of item types:", prioritySumValue)

# Day 3: Rucksack Reorganization Part 2 #

for i in range(0, len(rucksackList), 3):  # Divide rucksacks into elf groups, 3 rucksacks per group
    elfGroupsDictionary[i] = rucksackList[i:i + 3]

for key, rucksack in elfGroupsDictionary.items():
    common = list(set.intersection(*map(set, rucksack)))  # Find the common character in each group
    elfGroupBadgeList.append(common[0])  # Assign each group a badge

for matchingItem in elfGroupBadgeList:
    elfGroupPriorityValue += (priority[matchingItem])  # Sum of the badge value in each elf group

print("Sum of the priorities of each group item", elfGroupPriorityValue)
