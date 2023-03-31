from collections import defaultdict

with open("input/day7_input.txt") as f:
    commands = f.readlines()

sizes = defaultdict(int)
stack = []

for c in commands:
    if c.startswith("$ ls") or c.startswith("dir"):  # If the command starts with "$ ls" or "dir", skip it
        continue
    if c.startswith("$ cd"):   # If the command starts with "$ cd", change the current path
        destination = c.split()[2]  # Extract the directory from the command
        if destination == "..":   # If the destination is ".." move back one leve
            stack.pop()
        else:                        # Else, build a new path based on the last element in the stack and the destination directory
            path = f"{stack[-1]}_{destination}" if stack else destination
            stack.append(path)
    else:   # If the command does not start with "$ cd", it specifies a file with its size
        size, file = c.split() # Split the command into size and file
        for path in stack:  # Loop over each path in the stack and increment its size in the sizes dictionary by the value of size
            sizes[path] += int(size)

needed_size = 30000000 - (70000000 - sizes["/"])
for size in sorted(sizes.values()):
    if size > needed_size:
        break

print(sum(n for n in sizes.values() if n <= 100000))  # part 1
print(size) # part 2
