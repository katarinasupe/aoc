input = open("day-1/input.txt", "r")
lines = input.readlines()

max = 0
sum = 0

for line in lines:
    line_no_blanks = line.strip()
    if line_no_blanks:
        sum += int(line_no_blanks)
    else:
        if sum > max:
            max = sum
        sum = 0

print(max)
