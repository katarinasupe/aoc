# L=left, R=right; a=first elf, b=second elf
# La-Ra, Lb-Rb

# When does one range fully contain the other?
# CASE 1: La == Lb =>  elf a contains b, or the opposite
# CASE 2: La < Lb => only way is that elf a contains elf b
# and it follows that Ra >= Rb must be true
# CASE 3: La > Lb => only way is that elf b contains elf a
# and it follows that Ra <= Rb must be true

input = open("2022/day-4/input.txt", "r")
lines = input.readlines()
sum_1 = 0
sum_2 = 0


def is_in_range(L_a, R_a, L_b, R_b):
    if (L_a <= L_b and R_a >= R_b) or (L_a >= L_b and R_a <= R_b):
        return 1
    return 0


def is_in_range_2(L_a, R_a, L_b, R_b):
    if L_a <= R_b and R_a >= L_b:
        return 1
    return 0


for line in lines:
    first_elf, second_elf = line.strip().split(",")

    L_a, R_a = int(first_elf.split("-")[0]), int(first_elf.split("-")[1])
    L_b, R_b = int(second_elf.split("-")[0]), int(second_elf.split("-")[1])
    sum_1 += is_in_range(L_a, R_a, L_b, R_b)
    sum_2 += is_in_range_2(L_a, R_a, L_b, R_b)

print(sum_1)
print(sum_2)
