# Advent of code Year 2022 Day 3 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

import string

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

# Assign value to a-z A-Z
charPri = {}
priority = 1
for x in string.ascii_lowercase[:26]:
    charPri[x]=priority
    priority += 1

for x in string.ascii_uppercase[:26]:
    charPri[x]=priority
    priority += 1


#Part One
ruckSackPriority = 0
for line in input:
    partOne = set(line[:int(len(line)/2)])
    partTwo = (line[int(len(line)/2):])
    # Use intersect to fint characters present in both sets
    commonChars = partOne.intersection(partTwo)
    for char in commonChars:
        ruckSackPriority += charPri[char]

# Split lines
# Find common items
# Assign value and sum

print("Part One : "+ str(ruckSackPriority))

#Part One

print("Part Two : "+ str(None))