import collections
import utility

input = open("2022/day-3/input.txt", "r")
lines = input.readlines()

ctr = 0
sum = 0
groups = []
for line in lines:
    ctr += 1
    line = line.strip()
    groups.append(collections.Counter(line))
    if ctr % 3 == 0:
        intersection = set(groups[2].keys()).intersection(
            set(groups[0].keys()).intersection(set(groups[1].keys()))
        )
        sum += utility.get_priority(intersection.pop())
        ctr = 0
        groups = []

print(sum)
