def read_data(day):
    with open(f"data/day{day}/input.txt") as f:
        return [line.strip() for line in f.readlines()]
