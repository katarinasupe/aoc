from collections import Counter

file = "5.txt"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def overlapping_lines(file):
    with open(file) as f:
        input = f.readlines()
    points_on_line = list()
    for line in input:
        start_coord = line.split("->")[0].strip().split(",")
        start = Point(int(start_coord[0]), int(start_coord[1]))
        end_coord = line.split("->")[1].strip().split(",")
        end = Point(int(end_coord[0]), int(end_coord[1]))

        if start.x == end.x:
            if start.y > end.y:
                start, end = end, start  # swap
            for i in range(start.y, end.y + 1):
                points_on_line.append(Point(start.x, i))
        elif start.y == end.y:
            if start.x > end.x:
                start, end = end, start
            for i in range(start.x, end.x + 1):
                points_on_line.append(Point(i, start.y))

    counter = dict(Counter(points_on_line))

    sum = 0
    for key, value in counter.items():
        if value > 1:
            sum += 1
    print(sum)


def overlapping_diag(file):
    with open(file) as f:
        input = f.readlines()
    points_on_line = list()
    for line in input:
        start_coord = line.split("->")[0].strip().split(",")
        start = Point(int(start_coord[0]), int(start_coord[1]))
        end_coord = line.split("->")[1].strip().split(",")
        end = Point(int(end_coord[0]), int(end_coord[1]))

        if start.x == end.x:
            if start.y > end.y:
                start, end = end, start  # swap
            for i in range(start.y, end.y + 1):
                points_on_line.append(Point(start.x, i))
        elif start.y == end.y:
            if start.x > end.x:
                start, end = end, start
            for i in range(start.x, end.x + 1):
                points_on_line.append(Point(i, start.y))
        elif abs(start.x - end.x) == abs(start.y - end.y):
            if start.x > end.x:
                start, end = end, start
            diff = abs(start.x - end.x)
            for i in range(0, diff + 1):
                if start.y > end.y:
                    points_on_line.append(Point(start.x + i, start.y - i))
                elif start.y < end.y:
                    points_on_line.append(Point(start.x + i, start.y + i))

    counter = dict(Counter(points_on_line))

    sum = 0
    for key, value in counter.items():
        if value > 1:
            sum += 1
    print(sum)


def main():
    overlapping_lines(file)
    overlapping_diag(file)


if __name__ == "__main__":
    main()
