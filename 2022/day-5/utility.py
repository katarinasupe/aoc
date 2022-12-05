import re
from itertools import groupby


def get_moves(path: str):
    input_moves = open(path, "r")
    lines_moves = input_moves.readlines()

    all_moves = []
    for line in lines_moves:
        all_moves.append(re.findall(r"\d+", line.strip()))

    return all_moves


def solve(seq):
    for k, g in groupby(seq):
        length = sum(1 for _ in g)
        if k == "":
            for i in range(0, int(length / 4)):
                yield ""
        else:
            for i in range(0, length):
                yield k


def get_reversed_stacks(path: str):
    input = open(path, "r")
    lines = input.readlines()
    reversed_lines = reversed(lines)

    my_stacks = []
    for line in reversed_lines:
        stacks = line.replace("\n", "").split(" ")
        my_stacks.append(list(solve(stacks)))

    reversed_stacks = []
    for i in range(0, len(my_stacks[0])):
        new_stack = []
        for j in range(0, len(my_stacks)):
            current = my_stacks[j][i]
            if current != "":
                new_stack.append(my_stacks[j][i])
        reversed_stacks.append(new_stack)
    return reversed_stacks
