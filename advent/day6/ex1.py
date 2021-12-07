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


class Lanternfish:
    def __init__(self, timer):
        self.timer = timer

    def advance(self):
        if self.timer == 0:
            self.timer = 6
        else:
            self.timer -= 1

    def to_string(self) -> str:
        return f"<Lanternfish({self.timer})>"

    __str__ = to_string
    __repr__ = to_string


class Population:
    def __init__(self, fishies):
        self.fishies = fishies

    def to_string(self):
        timers = [str(fish.timer) for fish in self.fishies]
        return ",".join(timers)

    __str__ = to_string
    __repr__ = to_string

    @property
    def total_fish(self):
        return len(self.fishies)


def pass_day(pop):
    new_fish = []
    for fish in pop.fishies:
        if fish.timer == 0:
            new_fish.append(Lanternfish(8))
        fish.advance()
    pop.fishies.extend(new_fish)


def run():
    # data = TEST_DATA
    data = read_data(6)
    fishies = [Lanternfish(i) for i in map(int, data[0].split(","))]
    population = Population(fishies)

    days = 256

    # print(f"Initial state: {population}")
    for i in range(1, days + 1):
        fishies = pass_day(population)
        # print(f"After {i} days: {population}")

    print(f"Total fish: {population.total_fish}")
