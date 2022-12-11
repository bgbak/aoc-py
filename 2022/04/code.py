# Advent of code Year 2022 Day 4 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

# Split sections into sets
regex = r"(\d+)-(\d+),(\d+)-(\d+)"

overlap = 0
for line in input:
    #print("Processing {}".format(line))
    matches = re.findall(regex, line)[0]
    elf1Start = matches[0]
    elf1End = matches[1]
    elf2Start = matches[2]
    elf2End = matches[3]

    # Check if either range is contained in the other
    if (elf1Start <= elf2Start) and (elf1End >= elf2End):
        overlap += 1
    elif (elf2Start <= elf1Start) and (elf2End >= elf1End):
        overlap += 1

#Part One

print("Part One : "+ str(overlap))

#Part One

print("Part Two : "+ str(None))