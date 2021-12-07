import numpy as np

from advent.utils import read_data


TEST_DATA = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7",
]


class Board:
    def __init__(self, rows):
        self.matrix = np.array(rows)
        self.matches = self.matrix == None
        self.score = 0

    def mark(self, number):
        matches = self.matrix == number
        self.matches = np.where(matches, matches, self.matches)

    def check(self):
        x, y = self.matrix.shape
        for i in range(x):
            if self.matches[i, :].all():
                return True
        for j in range(y):
            if self.matches[:, j].all():
                return True
        return False

    @property
    def unmarked_sum(self):
        return self.matrix[~self.matches].sum()

    def calc_score(self, number):
        self.score = self.unmarked_sum * number

    def to_string(self):
        return str(self.matrix)

    __str__ = to_string
    __repr__ = to_string


def parse_data(data):
    numbers = list(map(int, data[0].split(",")))
    boards = []
    board = []
    for i, line in enumerate(data[2:]):
        if not line:
            boards.append(board)
            board = []
            continue
        board.append(list(map(int, line.split())))
        if i == len(data[2:]) - 1 and line:
            boards.append(board)
    return numbers, [Board(board) for board in boards]


def play_bingo(number, boards):
    for board in boards:
        board.mark(number)
    for board in boards:
        if board.check():
            board.calc_score(number)
            return board
    return None


def run():
    # data = TEST_DATA
    data = read_data(4)
    numbers, boards = parse_data(data)

    ranking = []
    for number in numbers:
        unfinished = [board for board in boards if not board.check()]
        round_winner = play_bingo(number, unfinished)
        if round_winner is None:
            continue
        ranking.append(round_winner)
        if len(ranking) == len(boards):
            break

    winning_board = ranking[0]
    losing_board = ranking[-1]

    assert winning_board is not None
    assert losing_board is not None

    print("Winning board:\n{}\n".format(winning_board))
    print("Matches:\n{}\n".format(winning_board.matches))
    print("Winning score: {}".format(winning_board.score))

    print("Losing board:\n{}\n".format(losing_board))
    print("Matches:\n{}\n".format(losing_board.matches))
    print("Losing score: {}".format(losing_board.score))
