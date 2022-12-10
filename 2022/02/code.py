# Advent of code Year 2022 Day 2 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

# Initialize roundOneScore
partOneScore = 0

hands = {
    "A":"ROCK",
    "B":"PAPER",
    "C":"SCISSORS",
    "ROCK":"X",
    "PAPER":"Y",
    "SCISSORS":"Z"
}


scores = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

winList = [
    "A Y",
    "B Z",
    "C X"
]

# Draw combos
drawList = [
    "A X",
    "B Y",
    "C Z"
]

def scoreRound(line):
    roundScore = 0
    # Did we win?
    if line in winList:
        roundScore += 6 
    elif line in drawList:
        roundScore += 3
    else:
        roundScore += 0

    # Score our pick
    roundScore += scores[hands[line[2]]]

    return roundScore

def scorePartTwo(line):
    roundScore = 0
    if line[2] == 'X':
        # Loose
        roundScore += 0
        # What do we need to play to loose?
        wePlay = hands["X"] 
    elif line[2] == 'Y':
        # Draw
        roundScore += 3
        # We need to play the same hand back
        

    elif line[2] == 'Z':
        # Win
        roundScore += 6
        # We need to beat the 
        

for line in input:

#Part One
    partOneScore += scoreRound(line)    

print("Part One : "+ str(partOneScore))

#Part Two


print("Part Two : "+ str(None))