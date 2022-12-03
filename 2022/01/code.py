# Advent of code Year 2022 Day 1 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

elfList = []
#Part One

# Iterate the input
currentElfCals = 0

for line in input:
    # If the line is not blank, add callories for our current elf.
    if line != "":
        currentElfCals += int(line)
    # Else output calories for the current elf to our list.
    else:
        elfList.append(currentElfCals)
        # Remember to reset the calorie counter.
        currentElfCals = 0

# Use the max() method to get max calories from the list
maxCalories = max(elfList)

# Print the number of the elf carrying the most calories.
print("Part One : "+ str(maxCalories))

#Part One
# Sort the list
elfList.sort(reverse=True)
# Add values for the top 3 indexes.
topElves = elfList[0] + elfList[1] + elfList [2]

print("Part Two : "+ str(topElves))