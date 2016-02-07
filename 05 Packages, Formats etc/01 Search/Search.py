import os
import sys


def main():
    file = sys.argv[1]
    location = sys.argv[2]
    if os.path.exists(location):
        check_files(file, location)


def check_files(file, loc):
    for root, dirs, files in os.walk(loc):
        for name in files:
            if name == file:
                print(os.path.join(root, name))
        for dir in dirs:
            check_files(file, dir)


if __name__ == "__main__":
    sys.exit(main())
