import re
import numpy as np

file = "4.txt"
ctr = 0
data = list()
with open(file) as f:
    numbers = [i for i in f.readline().split(",")]
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            ctr += 1
        else:
            data.append(line.split())

results = dict()
for i in range(0, ctr):
    results[i] = np.zeros((5, 5))

done = False
num = 0
for number in numbers:
    marked_positions = [(i, colour.index(number))
                        for i, colour in enumerate(data)
                        if number in colour]
    for position in marked_positions:
        pos = int(position[0] / 5)
        results[pos][position[0] % 5][position[1]] = 1
        # check rows
        if [1, 1, 1, 1, 1] in results[pos].tolist():
            print("Win by " + str(pos + 1))
            done = True
            winning_number = number
            break
        # check columns
        for i in range(0, 5):
            if results[pos][i][position[1]] == 1:
                num += 1
        if num == 5:
            print("Win by " + str(pos + 1))
            done = True
            winning_number = number
            break
        num = 0
    if done:
        break

sum = 0
for i in range(0, 5):
    for j in range(0, 5):
        if results[pos].astype(int).tolist()[i][j] == 0:
            sum += int(data[pos*5 + i][j])

print(sum * int(winning_number))

# part two -> figure out which board will win last
