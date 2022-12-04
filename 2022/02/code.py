# Advent of code Year 2022 Day 2 solution
# Author = Bj�rn Gustav Baklid
# Date = December 2018

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

'''
A - ROCK
B - PAPER
C - SCISSORS
X - ROCK - 1 point
Y - PAPER - 2 points
Z - SCISSORS - 3 points

WIN - 6
DRAW - 3
LOOSE - 0
'''

totalScore = 0

for line in input:

#Part One

    # Reset roundScore
    roundScore = 0
    
    # Only need lists for 2 of 3 outcomes 
    # Winning combos
    winList = [
        "A Z",
        "B X",
        "C Y"
    ]

    # Draw combos
    drawList = [
        "A X",
        "B Y",
        "C Z"
    ]

    # Did we win_
    if line in winList:
        roundScore += 6 
        print("We won!")
    elif line in drawList:
        roundScore += 3
        print("Draw...")
    else:
        print("We lost :(")

    # Score our pick
    if line[2] == 'X':
        roundScore += 1
        print("We picked rock. Add 1 to the score")
    elif line[2] == 'Y':
        roundScore += 2
        print("We picked paper. Add 2 to the score")
    elif line[2] == 'Z':
        roundScore += 3
        print("We picked scissors. Add 3 to the score")
    
    print("Round score: {}".format(str(roundScore)))
    totalScore += roundScore
    print("Our total score is now: {}".format(str(totalScore)))

print("Part One : "+ str(totalScore))

#Part One

print("Part Two : "+ str(None))