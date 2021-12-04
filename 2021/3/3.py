import re
file = "3.txt"


def to_decimal(bin):
    return sum([j*(2**i)
                for i, j in list(enumerate(reversed(bin)))])


def calc_power_consumption(input):
    column = list()
    gamma_rate = list()
    for col_ctr in range(0, 12):
        for line in input:
            column.append(int(line[col_ctr]))
        if sum(column) >= len(column)/2:
            gamma_rate.append(1)
        else:
            gamma_rate.append(0)
        column.clear()

    epsilon_rate = [int(not(bool(i))) for i in gamma_rate]

    print(to_decimal(gamma_rate) * to_decimal(epsilon_rate))


def oxygen_gen_rating(input):
    column = list()
    indices = [i for i in range(1000)]
    for col_ctr in range(0, 12):
        for line in input:
            column.append(int(line[col_ctr]))
        if sum(column) >= len(column)/2:
            indices = [i for i, x in enumerate(input) if x[col_ctr] == "1"]
        else:
            indices = [i for i, x in enumerate(input) if x[col_ctr] == "0"]
        if len(indices) == 1:
            ogr = list(map(int, (input[indices[0]].strip())))
            return ogr
        input = [input[i] for i in indices]
        column.clear()


def co2_scrubber_rating(input):
    column = list()
    indices = [i for i in range(1000)]
    for col_ctr in range(0, 12):
        for line in input:
            column.append(int(line[col_ctr]))
        if sum(column) < len(column)/2:
            indices = [i for i, x in enumerate(input) if x[col_ctr] == "1"]
        else:
            indices = [i for i, x in enumerate(input) if x[col_ctr] == "0"]
        if len(indices) == 1:
            ogr = list(map(int, (input[indices[0]].strip())))
            return ogr
        input = [input[i] for i in indices]
        column.clear()


def main():
    with open(file) as f:
        input = f.readlines()
    calc_power_consumption(input)
    print(to_decimal(oxygen_gen_rating(input)) *
          to_decimal(co2_scrubber_rating(input)))


if __name__ == "__main__":
    main()
