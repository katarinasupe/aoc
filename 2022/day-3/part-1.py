import collections
import utility

input = open("2022/day-3/input.txt", "r")
lines = input.readlines()

sum = 0
for line in lines:
    line = line.strip()
    firstpart, secondpart = collections.Counter(
        line[: len(line) // 2]
    ), collections.Counter(line[len(line) // 2 :])
    intersection = set(firstpart.keys()).intersection(set(secondpart.keys()))
    sum += utility.get_priority(intersection.pop())

print(sum)
