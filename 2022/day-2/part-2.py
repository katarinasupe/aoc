# X lose/Rock = 0/1
# Y draw/Paper = 3/2
# Z win/Scissors = 6/3

# A X -> play Z -> 3 + 0 = 3
# A Y -> play X -> 1 + 3 = 4
# A Z -> play Y -> 2 + 6 = 8
# B X -> play X -> 1 + 0 = 1
# B Y -> play Y -> 2 + 3 = 5
# B Z -> play Z -> 3 + 6 = 9
# C X -> play Y -> 2 + 0 = 2
# C Y -> play Z -> 3 + 3 = 6
# C Z -> play X -> 1 + 6 = 7

from enum import Enum


class Outcome(Enum):
    AX = 3
    AY = 4
    AZ = 8
    BX = 1
    BY = 5
    BZ = 9
    CX = 2
    CY = 6
    CZ = 7


input = open("day-2/input.txt", "r")
lines = input.readlines()

sum = 0

for line in lines:
    line_no_blanks = line.rstrip().replace(" ", "")
    sum += Outcome[line_no_blanks].value

print(sum)
