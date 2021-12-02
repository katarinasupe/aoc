file = "2.txt"
with open(file) as f:
    lines = f.readlines()

# ---PART ONE---
horizontal = 0
depth = 0
for line in lines:
    direction = line.rsplit()[0]
    amount = int(line.rsplit()[1])
    if direction == "forward":
        horizontal += amount
    elif direction == "down":
        depth += amount
    else:
        depth -= amount
print("Part one solution: " + str(horizontal * depth))


# ---PART TWO---
horizontal = 0
depth = 0
aim = 0
for line in lines:
    direction = line.rsplit()[0]
    amount = int(line.rsplit()[1])
    if direction == "forward":
        horizontal += amount
        depth += aim * amount
    elif direction == "down":
        aim += amount
    else:
        aim -= amount
print("Part two solution: " + str(horizontal * depth))
