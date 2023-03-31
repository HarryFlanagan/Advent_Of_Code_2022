# --- Day 6: Tuning Trouble ---
# Read Input File
with open('input/day6_Input.txt', 'r') as file:
    input = file.read().rstrip()
lettersList = [*input[0:14]]
for n in range(len(input)):
    lettersList = [*input[n:n+14]]
    if len(set(lettersList)) == len(lettersList):
        print("How many characters need to be processed before the first start-of-packet marker is detected?:", n+14)
        break


