# Advent of code Year 2022 Day 5 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

# Containers
containers = input[:7]
instructions = input[10:]

# Find index of stacks
stackIndex = {}
for x in input[8]:
    if x != " ":
        stackIndex[x] = input[8].index(x)

# Create lists of stacks
for line in containers:
    for x in stackIndex:


#Part One

print("Part One : "+ str(None))

#Part One

print("Part Two : "+ str(None))