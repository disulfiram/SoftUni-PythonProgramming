import sys
import math


_LOSS = 1.098


def main():
    try:
        sheet_area = 0.0
        height = 0.0
        width = 0.0
        depth = 0.0
        try:
            sheet_area = float(input())
            height = float(input())
            width = float(input())
            depth = float(input())
        except:
            raise InvalidInputException
        area = (2*width*height)+(2*height*depth)+(2*depth*width)
        print(math.ceil((area/sheet_area)*_LOSS))
    except InvalidInputException:
        print("INVALID INPUT")


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
