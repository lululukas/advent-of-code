from advent.utils import read_data


TEST_DATA = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

POSITIONS = {i: letter for i, letter in enumerate("abcdefg")}
ZERO = "1110111"
ONE = "0010010"
TWO = "1011101"
THREE = "1011011"
FOUR = "0111010"
FIVE = "1101011"
SIX = "1101111"
SEVEN = "1010010"
EIGHT = "1111111"
NINE = "1111011"
DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
SEGMENT_COUNTS = {}
for i in range(7):
    count = 0
    for digit in DIGITS:
        if digit[i] == "1":
            count += 1
    SEGMENT_COUNTS[i] = count


def count_segments(inputs):
    counts = {}
    for letter in "abcdefg":
        count = 0
        for digit in inputs:
            count += digit.count(letter)
        counts[letter] = count
    return counts


def get_digit_by_length(inputs, count):
    parsed_digit = [i for i in inputs if len(i) == count]
    assert len(parsed_digit) == 1
    return parsed_digit[0]


def get_digit_from_mapping(digit, mapping):
    pattern = DIGITS[digit]
    return "".join(sorted([mapping[i] for i, q in enumerate(pattern) if q == "1"]))


def parse_inputs(inputs):
    pos_letter_mapping = {}
    one = get_digit_by_length(inputs, 2)
    four = get_digit_by_length(inputs, 4)
    seven = get_digit_by_length(inputs, 3)
    eight = get_digit_by_length(inputs, 7)
    for segment in seven:
        if segment not in one:
            pos_letter_mapping[0] = segment
            break
    segment_counts = count_segments(inputs)
    for segment, count in segment_counts.items():
        if count == 6:
            pos_letter_mapping[1] = segment
        elif count == 4:
            pos_letter_mapping[4] = segment
        elif count == 9:
            pos_letter_mapping[5] = segment
        elif count == 8 and segment != pos_letter_mapping[0]:
            pos_letter_mapping[2] = segment
    for segment in [segment for segment, count in segment_counts.items() if count == 7]:
        if segment in four:
            pos_letter_mapping[3] = segment
        else:
            pos_letter_mapping[6] = segment
    zero = get_digit_from_mapping(0, pos_letter_mapping)
    assert zero in inputs
    two = get_digit_from_mapping(2, pos_letter_mapping)
    assert two in inputs
    three = get_digit_from_mapping(3, pos_letter_mapping)
    assert three in inputs
    five = get_digit_from_mapping(5, pos_letter_mapping)
    assert five in inputs
    six = get_digit_from_mapping(6, pos_letter_mapping)
    assert six in inputs
    nine = get_digit_from_mapping(9, pos_letter_mapping)
    assert nine in inputs
    return pos_letter_mapping, {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}


def count_recognizable(output):
    count = 0
    for segment in output.split():
        if 1 < len(segment) < 5 or len(segment) == 7:
            count += 1
    return count


def run():
    #data = TEST_DATA
    data = read_data(8)
    lines = []
    for line in data:
        inputs, outputs = line.split(" | ")
        lines.append((inputs, outputs))

    results = []
    for inputs, outputs in lines:
        inputs = ["".join(sorted(i)) for i in inputs.split()]
        outputs = ["".join(sorted(o)) for o in outputs.split()]
        pos_mapping, digits = parse_inputs(inputs)
        reverse_digits = {v: k for k, v in digits.items()}
        number = ""
        for output in outputs:
            digit = reverse_digits[output]
            number += str(digit)
        results.append(int(number))

    print(results)
    print(f"Sum of outputs: {sum(results)}")
