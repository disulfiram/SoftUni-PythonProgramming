import sys
import math


_COVERAGE = 1.76


def main():
    width = float(input())
    height = float(input())
    area = width*height
    print(math.ceil(area/_COVERAGE))


if __name__ == "__main__":
    sys.exit(main())
