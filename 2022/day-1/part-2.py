input = open("2022/day-1/input.txt", "r")
lines = input.readlines()


def compare(sum, top_three):
    if sum >= top_three[2]:
        top_three = (top_three[1], top_three[2], sum)
    elif sum >= top_three[1]:
        top_three = (top_three[1], sum, top_three[2])
    elif sum >= top_three[0]:
        top_three = (sum, top_three[1], top_three[2])

    return top_three


max = 0
sum = 0
top_three = (0, 0, 0)  # 3., 2., 1.; min -> max
for line in lines:
    line_no_blanks = line.strip()
    if line_no_blanks:
        sum += int(line_no_blanks)
    else:
        top_three = compare(sum, top_three)
        sum = 0

top_three = compare(sum, top_three)

print(top_three)
print(top_three[0] + top_three[1] + top_three[2])
