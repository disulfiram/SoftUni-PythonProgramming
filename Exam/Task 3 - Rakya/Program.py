import sys
import os
import math


def main():
    try:
        alcohol = 0.0
        try:
            alcohol = float(input())
        except:
            raise InvalidInputException
        jugs_file = input()
        if not os.path.isfile(jugs_file):
            raise InvalidInputException
        file_valid = False
        jugs = {}
        with open(jugs_file, encoding="utf-8") as f:
            for row in f:
                stripped_row = row.strip()
                if stripped_row == "":
                    continue
                values = row.split(sep=',')
                if values[0] in jugs:
                    raise InvalidInputException
                try:
                    r = float(values[1])
                    h = float(values[2])
                except:
                    raise InvalidInputException
                jugs[values[0]] = math.pi * math.pow(r,2) * h
                file_valid = True
        if not file_valid:
            raise InvalidInputException

        name_of_jug = "NO SUITABLE CONTAINER"
        for jug in jugs:
            if jugs[jug] > alcohol*1000 and (name_of_jug == "NO SUITABLE CONTAINER" or jugs[jug] < jugs[name_of_jug]):
                name_of_jug = jug
        print(name_of_jug)

    except InvalidInputException:
        print("INVALID INPUT")


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
