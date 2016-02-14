import sys
import os


def main():
    try:
        movement_file = input()
        if not os.path.isfile(movement_file):
            raise InvalidInputException
        position = [0.0,0.0]
        file_valid = False
        with open(movement_file) as f:
            for row in f:
                if row.strip() == "":
                    continue
                direction = row.split()[0]
                step = 0.0
                try:
                    step = float(row.split()[1])
                except:
                    raise InvalidInputException
                if direction == "up":
                    position[1] += step
                elif direction == "down":
                    position[1] -= step
                elif direction == "right":
                    position[0] += step
                elif direction == "left":
                    position[0] -= step
                else:
                    raise InvalidInputException
                file_valid = True
        if not file_valid:
            raise InvalidInputException
        print("X {:.3f}".format(position[0]))
        print("Y {:.3f}".format(position[1]))
    except InvalidInputException:
        print("INVALID INPUT")


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
