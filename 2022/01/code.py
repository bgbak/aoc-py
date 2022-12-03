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
print('Max calories: {}'.format(maxCalories))
# Get the index of the elf with the most calories
elfNo = elfList.index(maxCalories)
print("Index with max calories: {}".format(elfList[elfNo]))
print("Calories carried on index {} : {}".format(elfNo,elfList[elfNo]))

# Print the number of the elf carrying the most calories.
print("Part One : "+ str(elfNo))

#Part One

print("Part Two : "+ str(None))