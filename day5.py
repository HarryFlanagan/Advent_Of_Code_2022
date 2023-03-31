# Day 5: Supply Stacks Part 1 #
with open("input/day5_input.txt", "r") as f:
    instructions = f.readlines()[10:]

cols = [
    ['[N]', '[H]', '[S]', '[J]', '[F]', '[W]', '[T]', '[D]'],
    ['[G]', '[B]', '[N]', '[T]', '[Q]', '[P]', '[R]', '[H]'],
    ['[V]', '[Q]', '[L]'],
    ['[Q]', '[R]', '[W]', '[S]', '[B]', '[N]'],
    ['[B]', '[M]', '[V]', '[T]', '[F]', '[D]', '[N]'],
    ['[R]', '[T]', '[H]', '[V]', '[B]', '[D]', '[M]'],
    ['[J]', '[Q]', '[B]', '[D]'],
    ['[Q]', '[H]', '[Z]', '[R]', '[V]', '[J]', '[N]', '[D]'],
    ['[S]', '[M]', '[H]', '[N]', '[B]'],
]

print("-------Starting columns-------")
for col in cols:
    print(col)
print("------------------------------")

# example instruction: move 3 from 1 to 2
for instruction in instructions:
    numberOfCratesToMove = int(instruction.split()[1])
    moveFromStack = (int(instruction.split()[3]) - 1)
    moveToStack = (int(instruction.split()[5]) - 1)

    crane = cols[moveFromStack][0:numberOfCratesToMove]
    cols[moveFromStack] = cols[moveFromStack][numberOfCratesToMove:]
    # comment our crane_revered and replace crane_reversed with crane in for loop to have code work for part 1
    crane_reversed = list(reversed(crane))
    for i in crane_reversed:
        cols[moveToStack].insert(0, i)

print("-------Finished columns-------")
for col in cols:
    print(col)
print("------------------------------")
