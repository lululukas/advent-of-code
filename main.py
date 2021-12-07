import argparse
import sys

import advent


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("problem", type=int)
    return parser.parse_args()


def main():
    args = get_args()
    day = getattr(advent, f"day{args.day}")
    prob = getattr(day, f"ex{args.problem}")
    prob.run()


if __name__ == "__main__":
    status = main()
    sys.exit(status)
