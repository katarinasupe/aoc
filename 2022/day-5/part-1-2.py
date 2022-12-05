import utility


def run_crate_mover(is_reversed=True):
    stacks_path = "2022/day-5/input-stacks.txt"
    moves_path = "2022/day-5/input-moves.txt"
    utility.parse_input("2022/day-5/input.txt", stacks_path, moves_path)
    stacks = utility.get_reversed_stacks(stacks_path)
    moves = utility.get_moves(moves_path)

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
