import sys
import os


def main():
    if len(sys.argv) < 3:
        print("Usage: {} {{catalog csv file}} {{sales csv file}}".format(sys.argv[0]))
        return 0

if __name__ == "__main__":
    sys.exit(main())