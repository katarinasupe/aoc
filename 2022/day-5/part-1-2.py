import utility


def run_crate_mover(is_reversed=True):
    moves = utility.get_moves("2022/day-5/input_moves.txt")
    stacks = utility.get_reversed_stacks("2022/day-5/input_stacks.txt")

    for move in moves:
        moved_crates = stacks[int(move[1]) - 1][-int(move[0]) :]
        if is_reversed:
            for crate in list(reversed(moved_crates)):
                stacks[int(move[2]) - 1].append(crate)
        else:
            for crate in moved_crates:
                stacks[int(move[2]) - 1].append(crate)
        stacks[int(move[1]) - 1] = stacks[int(move[1]) - 1][: -int(move[0])]

    for stack in stacks:
        print(stack[len(stack) - 1])


run_crate_mover()
print()
run_crate_mover(False)
