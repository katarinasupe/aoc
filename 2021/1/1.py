file = "1.txt"
increased = 0
with open(file) as f:
    lines = f.readlines()
lines = [int(line) for line in lines]
previous = lines[0]
for i in range(1, len(lines)):
    if lines[i] > previous:
        increased += 1
    previous = lines[i]
print(increased)

previous_sum = lines[0] + lines[1] + lines[2]
increased_three = 0
for j in range(1, len(lines) - 2):
    sum_next = lines[j] + lines[j+1] + lines[j+2]
    if sum_next > previous_sum:
        increased_three += 1
    previous_sum = sum_next
print(increased_three)
