def find_marker(path, num_of_chars):
    text = open(path).read()
    ctr = num_of_chars
    length = len(text)

    while ctr < length:
        chars = text[:num_of_chars]
        if len(set(chars)) == len(chars):
            return ctr
        else:
            ctr += 1
            text = text[1:]

    return "Not found"


# print(find_marker("/Users/katelatte/repos/aoc/2022/day-6/test.txt", 4))
print(find_marker("/Users/katelatte/repos/aoc/2022/day-6/input.txt", 14))
