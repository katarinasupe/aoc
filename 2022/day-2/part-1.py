# rock - A / X = 1
# paper - B / Y = 2
# scissors - C / Z = 3

# lose = 0
# draw = 3
# win = 6

# loses => rock > scissors = A Z -> 3 + 0 = 3
#      => paper > rock = B X -> 1 + 0 = 1
#      => scissors > paper C Y -> 2 + 0 = 2
# draws => rock = rock = A X -> 1 + 3 = 4
#       => paper = paper = B Y -> 2 + 3 = 5
#       => scissor = scissor = C Z -> 3 + 3 = 6
# wins => rock < paper = A Y -> 2 + 6 = 8
#       => paper < scissors = B Z -> 3 + 6 = 9
#       => scissors < rock = C X -> 1 + 6 = 7
# total = wins + draws + loses


from enum import Enum


class Outcome(Enum):
    AZ = 3
    BX = 1
    CY = 2
    AX = 4
    BY = 5
    CZ = 6
    AY = 8
    BZ = 9
    CX = 7


input = open("day-2/input.txt", "r")
lines = input.readlines()

sum = 0

for line in lines:
    line_no_blanks = line.rstrip().replace(" ", "")
    sum += Outcome[line_no_blanks].value

print(sum)
