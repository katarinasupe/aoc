lines = open("2022/day-7/input.txt").readlines()

TOTAL_DISK_SPACE = 70000000
MIN_UNUSED_SPACE = 30000000


class Commands:
    CD = "cd"
    LS = "ls"
    START = "$"
    DIR = "dir"


class Arguments:
    BACK = ".."
    ROOT = "/"


def update_dir_size(dir_sizes, dir, file_size):
    if dir in dir_sizes.keys():
        dir_sizes[dir] += file_size
    else:
        dir_sizes[dir] = file_size


def get_path(parent, child):
    if parent == Arguments.ROOT:
        return parent + child
    else:
        return parent + "/" + child


def add_child(parent_to_children, parent, child):
    if parent in parent_to_children.keys():
        parent_to_children[parent].add(get_path(parent, child))
    else:
        parent_to_children[parent] = {get_path(parent, child)}


# parent_to_children -> dict {parent_dir: [child_dir]}
# dir_sizes -> dict {dir: size}
parent_to_children = {}
dir_sizes = {}
path = []
parent_dir = Arguments.ROOT
current_dir = ""
for line in lines:
    # if CD or LS
    if line.startswith(Commands.START):
        command = line.rstrip().split(" ")[1]
        if command == Commands.CD:
            argument = line.rstrip().split(" ")[2]

            if argument == Arguments.BACK:
                current_dir = current_dir.rsplit("/", 1)[0]

            else:  # cd dir (subdirectories of different dirs can have same names)
                if argument == Arguments.ROOT:
                    current_dir = argument
                else:
                    current_dir = get_path(current_dir, argument)
                path.append(current_dir)
                # initialize size to 0
                update_dir_size(dir_sizes, current_dir, 0)
        # else do nothing (LS)

    elif line.startswith(Commands.DIR):
        child = line.rstrip().split(" ")[1]
        add_child(parent_to_children, current_dir, child)

    else:  # size + file
        file_size = int(line.split()[0])
        update_dir_size(dir_sizes, current_dir, file_size)

print(parent_to_children)
print(dir_sizes)

total_dir_sizes = {}


def get_dir_size(dir):

    if dir not in parent_to_children.keys():
        leaf_size = dir_sizes[dir]
        total_dir_sizes[dir] = leaf_size
    else:
        children_size = 0
        children = parent_to_children[dir]

        for child in children:
            get_dir_size(child)
            children_size += total_dir_sizes[child]

        total_dir_size = dir_sizes[dir] + children_size
        total_dir_sizes[dir] = total_dir_size


get_dir_size("/")
print(total_dir_sizes)
print(sum(v for k, v in total_dir_sizes.items() if v <= 100000))
print("Unused space is", TOTAL_DISK_SPACE - total_dir_sizes[Arguments.ROOT])

total_root_size = total_dir_sizes[Arguments.ROOT]
unused_space = TOTAL_DISK_SPACE - total_root_size

potential_deletes = {}
for dir in total_dir_sizes.keys():
    dir_size = total_dir_sizes[dir]
    if unused_space + dir_size >= MIN_UNUSED_SPACE:
        potential_deletes[dir] = dir_size

lowest = min(potential_deletes, key=potential_deletes.get)

print(lowest, potential_deletes[lowest])
