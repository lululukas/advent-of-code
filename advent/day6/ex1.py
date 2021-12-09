import collections

from advent.utils import read_data


"""
Initial state: 3,4,3,1,2
After  1 day:  2,3,2,0,1
After  2 days: 1,2,1,6,0,8
After  3 days: 0,1,0,5,6,7,8
After  4 days: 6,0,6,4,5,6,7,8,8
After  5 days: 5,6,5,3,4,5,6,7,7,8
After  6 days: 4,5,4,2,3,4,5,6,6,7
After  7 days: 3,4,3,1,2,3,4,5,5,6
After  8 days: 2,3,2,0,1,2,3,4,4,5
After  9 days: 1,2,1,6,0,1,2,3,3,4,8
After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
"""

TEST_DATA = ["3,4,3,1,2"]
NEW_FISH = 6
BIRTH_FISH = 8


def evolve_fish(fishes):
    fishes = {k - 1: v for k, v in fishes.items()}
    new_fishies = fishes.pop(-1, 0)
    fishes[BIRTH_FISH] = fishes.get(BIRTH_FISH, 0) + new_fishies
    fishes[NEW_FISH] = fishes.get(NEW_FISH, 0) + new_fishies
    return fishes


def run():
    #data = TEST_DATA
    data = read_data(6)
    fishies = collections.Counter(map(int, data[0].split(",")))

    days = 256

    # print(f"Initial state: {population}")
    for i in range(1, days + 1):
        fishies = evolve_fish(fishies)
        # print(f"After {i} days: {population}")

    print(f"Total fish: {sum(fishies.values())}")
