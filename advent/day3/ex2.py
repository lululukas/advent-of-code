from advent.utils import read_data


TEST_NUMBERS = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def most_common_bit(numbers, pos):
    bits = [number[pos] for number in numbers]
    return "1" if bits.count("1") >= bits.count("0") else "0"


def least_common_bit(numbers, pos):
    bits = [number[pos] for number in numbers]
    return "1" if bits.count("1") < bits.count("0") else "0"


class Rating:
    def get_criteria(self, numbers, pos):
        raise NotImplementedError

    def match(self, bit, criteria):
        return bit == criteria


class O2Rating(Rating):
    def get_criteria(self, numbers, pos):
        return most_common_bit(numbers, pos)


class CO2Rating(Rating):
    def get_criteria(self, numbers, pos):
        return least_common_bit(numbers, pos)


def find_number(numbers, rating, pos=0):
    criteria = rating.get_criteria(numbers, pos)
    if pos > len(numbers[0]):
        raise RuntimeError("Could not reduce numbers to 1")
    numbers = list(filter(lambda n: rating.match(n[pos], criteria), numbers))
    if len(numbers) == 1:
        return numbers[0]
    return find_number(numbers, rating, pos + 1)


def run():
    numbers = read_data(3)
    # numbers = TEST_NUMBERS
    o2_rating = find_number(numbers, O2Rating())
    co2_rating = find_number(numbers, CO2Rating())

    print(f"O2 rating: {o2_rating}")
    print(f"CO2 rating: {co2_rating}")

    life_support = int(o2_rating, 2) * int(co2_rating, 2)
    print(f"Life support rating: {life_support}")

    return int(o2_rating, 2) * int(co2_rating, 2)
