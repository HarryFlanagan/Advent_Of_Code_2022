# Day 4: Camp Cleanup Part 1 #
import re

# Read Input File
with open('input/day4_input.txt') as i:
    assignments = i.read().splitlines()

counter = 0

for assignment in assignments:

    assignmentSplit = re.split(',|-', assignment)
    assignmentSplit1 = list(range(int(assignmentSplit[0]), int(assignmentSplit[1]) + 1))
    assignmentSplit2 = list(range(int(assignmentSplit[2]), int(assignmentSplit[3]) + 1))

    if (set(assignmentSplit1).issubset(assignmentSplit2)) or (set(assignmentSplit2).issubset(assignmentSplit1)):
        counter += 1

print("number of completely overlapping assignments: ", counter)

# Day 4: Camp Cleanup Part 2 #

counter = 0

for assignment in assignments:

    assignmentSplit = re.split(',|-', assignment)
    assignmentSplit1 = list(range(int(assignmentSplit[0]), int(assignmentSplit[1]) + 1))
    assignmentSplit2 = list(range(int(assignmentSplit[2]), int(assignmentSplit[3]) + 1))

    if any(x in assignmentSplit1 for x in assignmentSplit2):
        counter += 1

print("number of semi overlapping assignments: ", counter)