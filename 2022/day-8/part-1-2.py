import numpy as np

lines = open("2022/day-8/input.txt").readlines()


def is_visible(current_tree, section):
    if np.all([True if current_tree > tree else False for tree in section]):
        return 1
    return 0


data = []
scenic_scores = []
for line in lines:
    strip_line = line.rstrip()
    data.append([int(x) for x in strip_line])

visible_ctr = 2 * (len(data) + len(data[0]) - 2)
data_transposed = np.array(data).transpose()

for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        current_tree = data[i][j]

        right_trees = data[i][j + 1 :]
        left_trees = data[i][:j]
        upper_trees = data_transposed[j][:i]
        lower_trees = data_transposed[j][i + 1 :]

        # PART 2
        # initialize directions
        left = right = up = down = -1

        # left direction
        it = len(left_trees) - 1
        while it != -1:
            if current_tree <= left_trees[it]:
                left = j - it
                break
            it -= 1
        if left == -1:
            left = len(left_trees)

        # right direction
        it = 0
        while it != len(right_trees):
            if current_tree <= right_trees[it]:
                right = it + 1
                break
            it += 1
        if right == -1:
            right = len(right_trees)

        # up direction
        it = len(upper_trees) - 1
        while it != -1:
            if current_tree <= upper_trees[it]:
                up = len(upper_trees) - it
                break
            it -= 1
        if up == -1:
            up = len(upper_trees)

        # down direction
        it = 0
        while it != len(lower_trees):
            if current_tree <= lower_trees[it]:
                down = it + 1
                break
            it += 1
        if down == -1:
            down = len(lower_trees)

        scenic_score = left * right * up * down
        scenic_scores.append(scenic_score)

        # PART 1
        if is_visible(current_tree, right_trees):
            visible_ctr += 1
            continue
        if is_visible(current_tree, left_trees):
            visible_ctr += 1
            continue
        if is_visible(current_tree, upper_trees):
            visible_ctr += 1
            continue
        if is_visible(current_tree, lower_trees):
            visible_ctr += 1
            continue


print("Number of visible trees is", visible_ctr)
print("The highest scenic score possible is", max(scenic_scores))
