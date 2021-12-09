from collections import Counter
import numpy as np

from advent.utils import read_data


TEST_DATA = [
    "16,1,2,0,4,2,7,1,2,14"
]


def calc_fuel(candidate, position, n):
    moves = abs(candidate - position)
    fuel = sum(range(1, moves + 1))
    return fuel * n


def align(init_positions):
    median = np.median(init_positions)
    if not median.is_integer():
        raise ValueError("Not an integer")
    return int(median)


def align2(init_positions):
    position_counts = Counter(init_positions)
    costs = {}
    for candidate in range(max(init_positions)):
        cost = 0
        for pos, n in position_counts.items():
            cost += calc_fuel(candidate, pos, n)
        costs[candidate] = cost
    return sorted(costs.items(), key=lambda x: x[1])[0]


def run():
    data = read_data(7)
    #data = TEST_DATA
    init_positions = [int(i) for i in data[0].split(",")]
    position, fuel_cost = align2(init_positions)
    print("Align on position {} for a fuel cost of {}".format(
        position, fuel_cost)
    )
