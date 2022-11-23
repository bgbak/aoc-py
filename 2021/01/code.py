# Advent of code Year 2021 Day 1 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    #input = input_file.read().splitlines()
    depths = input_file.read().splitlines()

count = 0
for i in range(len(depths)-1):
    if depths[i] < depths[i+1]:
        count += 1

print("Part One : "+ str(count))


print("Part Two : "+ str(None))