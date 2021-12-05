import numpy as np


def get_boards():
    file = "4.txt"
    num_of_boards = 0
    data = list()
    with open(file) as f:
        numbers = [i for i in f.readline().split(",")]
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                num_of_boards += 1
            else:
                data.append(line.split())
        return numbers, data, num_of_boards


def prepare_results(num_of_boards):
    results = dict()
    for i in range(0, num_of_boards):
        results[i] = np.zeros((5, 5))
    return results


def get_winner(results, numbers, data):
    sum = 0
    for number in numbers:
        marked_positions = [(i, colour.index(number))
                            for i, colour in enumerate(data)
                            if number in colour]
        for position in marked_positions:
            pos = int(position[0] / 5)
            results[pos][position[0] % 5][position[1]] = 1
            # check rows
            if [1, 1, 1, 1, 1] in results[pos].tolist():
                print("First winner is board number " + str(pos + 1) + "!")
                return number, pos
            # check columns
            for i in range(0, 5):
                if results[pos][i][position[1]] == 1:
                    sum += 1
            if sum == 5:
                print("First winner is board number " + str(pos + 1) + "!")
                return number, pos
            sum = 0


def get_score(results, data, pos, winner):
    sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if results[pos].astype(int).tolist()[i][j] == 0:
                sum += int(data[pos*5 + i][j])
    return sum * winner


def prepare_losers(data):
    board_number = 0
    losers = dict()
    loser_list = list()
    for el in data:
        loser_list.append(el)
        if len(loser_list) == 5:
            losers[board_number] = loser_list.copy()
            loser_list.clear()
            board_number += 1
    return losers


def get_loser(losers, results, data, numbers):
    sum = 0
    last_called_num_pos = 0
    for number in numbers:
        marked_positions = [(i, row.index(number))
                            for i, row in enumerate(data)
                            if number in row]
        for position in marked_positions:
            pos = int(position[0] / 5)
            results[pos][position[0] % 5][position[1]] = 1
            # check rows
            if [1, 1, 1, 1, 1] in results[pos].tolist():
                if pos in losers:
                    removed_value = losers.pop(pos)
            # check columns
            for i in range(0, 5):
                if results[pos][i][position[1]] == 1:
                    sum += 1
            if sum == 5:
                winning_number = number
                if pos in losers:
                    removed_value = losers.pop(pos)
            sum = 0
            if len(losers) == 1:
                return losers, last_called_num_pos, pos, position
        last_called_num_pos += 1


def get_loser_win(last_called_num_pos, numbers, loser, loser_board, results, pos, position):
    num = 0
    for i in range(last_called_num_pos + 1, len(numbers)):
        number = numbers[i]
        marked_positions = [(i, row.index(number))
                            for i, row in enumerate(list(loser[loser_board]))
                            if number in row]
        if len(marked_positions) > 0:
            row = marked_positions[0][0]
            col = marked_positions[0][1]
            results[loser_board][row][col] = 1
            if [1, 1, 1, 1, 1] in results[loser_board].tolist():
                return number
            for i in range(0, 5):
                if results[pos][i][position[1]] == 1:
                    num += 1
            if num == 5:
                return number
        num = 0


def main():
    numbers, data, num_of_boards = get_boards()
    results = prepare_results(num_of_boards)
    winner, pos = get_winner(results, numbers, data)
    score = get_score(results, data, pos, int(winner))
    print("Its score is " + str(score) + ".")
    losers = prepare_losers(data)
    loser, last_called_num_pos, pos, position = get_loser(
        losers, results, data, numbers)
    loser_board = list(loser.keys())[0]
    winning_number = get_loser_win(last_called_num_pos, numbers, loser,
                                   loser_board, results, pos, position)
    print("Last loser is board number " + str(loser_board+1) + ".")
    print("The score of its win would be " +
          str(get_score(results, data, loser_board, int(winning_number))) + ".")


if __name__ == "__main__":
    main()
