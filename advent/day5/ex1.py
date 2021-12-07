import collections
from typing import List

import numpy as np

from advent.utils import read_data


TEST_DATA = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @property
    def coordinates(self) -> tuple:
        return self.x, self.y

    def __eq__(self, other: "Point") -> bool:
        return self.coordinates == other.coordinates

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self) -> int:
        return hash(self.coordinates)

    def to_string(self) -> str:
        return f"<Point({self.x}, {self.y})>"

    __str__ = to_string
    __repr__ = to_string

    @classmethod
    def from_string(cls, string) -> "Point":
        x, y = tuple(map(int, string.split(",")))
        return Point(x, y)


class Line:
    def __init__(self, point1: Point, point2: Point):
        ordered_points = sorted([point1, point2], key=lambda p: p.x)
        self.point1 = ordered_points[0]
        self.point2 = ordered_points[1]
        self.distance = point2 - point1

    def to_string(self) -> str:
        return f"<Line({self.point1}, {self.point2})>"

    __str__ = to_string
    __repr__ = to_string

    @property
    def is_horizontal(self) -> bool:
        return self.point1.y == self.point2.y

    @property
    def is_vertical(self) -> bool:
        return self.point1.x == self.point2.x

    @property
    def slope(self) -> float:
        if self.is_horizontal:
            return 0.0
        elif self.is_vertical:
            return float("inf")
        return self.distance.y / self.distance.x

    @property
    def points_covered(self) -> List[Point]:
        points = []
        if self.is_vertical:
            sign = 1 if self.distance.y < 0 else 0
            for i in range(1, abs(self.distance.y)):
                i = i if not sign else -i
                point = Point(self.point1.x, self.point1.y + i)
                points.append(point)
        else:
            # sign_x = 1 if self.distance.x < 0 else 0
            # sign_y = 1 if self.distance.y < 0 else 0
            if not self.slope.is_integer():
                raise ValueError("Slope is not 0, 1, or inf")
            slope = int(self.slope)
            point = self.point1
            for i in range(1, abs(self.distance.x)):
                # xchange = -1 if sign_x else 1
                # ychange = -1 * slope if sign_y else slope
                point = point + Point(1, slope)
                points.append(point)
        return [self.point1, *points, self.point2]


def parse_data(data):
    lines = []
    for line in data:
        c1, c2 = line.split(" -> ")
        lines.append(Line(Point.from_string(c1), Point.from_string(c2)))
    return lines


def get_matrix(lines: List[Line]):
    matrix = np.zeros((1000, 1000))
    for line in lines:
        for point in line.points_covered:
            matrix[point.y, point.x] += 1
    return matrix


def plot_matrix(matrix):
    plot_data = []
    for i in matrix:
        row = []
        for j in i:
            row.append(str(int(j)) if j != 0 else ".")
        plot_data.append("".join(row))
    diagram = "\n".join(plot_data)
    return diagram


def run():
    # data = TEST_DATA
    data = read_data(5)
    lines = parse_data(data)

    # lines = list(filter(lambda line: line.is_vertical or line.is_horizontal, lines))

    matrix = get_matrix(lines)
    print(plot_matrix(matrix))

    over_x, over_y = np.where(matrix > 1)
    overlapping = [Point(x, y) for x, y in zip(over_x, over_y)]
    print("Overlapping points: {}".format(overlapping))
    print("Sum of overlaps: {}".format((matrix > 1).sum()))
