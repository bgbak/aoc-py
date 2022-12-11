# Advent of code Year 2022 Day 4 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018


with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()



contained = 0
overlap = 0
for line in input:
    # ditched regex and stole string split from someone else.
    elf1,elf2=line.split(",")
    elf1Start,elf1End = [int(r) for r in elf1.split("-")]
    elf2Start,elf2End = [int(r) for r in elf2.split("-")]

    # Check if either range is contained in the other
    if (elf1Start <= elf2Start) and (elf1End >= elf2End):
        contained += 1
    elif (elf2Start <= elf1Start) and (elf2End >= elf1End):
        contained += 1
    elif  ()

#Part One

print("Part One : "+ str(contained))

#Part One

print("Part Two : "+ str(None))