from advent.utils import read_data


data = read_data(2)

#data = [
#    "forward 5",
#    "down 5",
#    "forward 8",
#    "up 3",
#    "down 8",
#    "forward 2"
#]
instructions = [line.split() for line in data]
#print(instructions)


class Submarine:
    aim = 0
    x = 0
    y = 0

    def move_forward(self, units):
        self.x += units
        self.y += self.aim * units

    def move_up(self, units):
        self.aim -= units

    def move_down(self, units):
        self.aim += units

    def move(self, direction, units):
        method = {
            "forward": self.move_forward,
            "up": self.move_up,
            "down": self.move_down
        }[direction]
        method(units)


def main():
    sub = Submarine()
    for direction, units in instructions:
        sub.move(direction, int(units))
        print(sub.x, sub.y, sub.aim)

    print(sub.x, sub.y)
    print(sub.x * sub.y)


if __name__ == "__main__":
    main()

