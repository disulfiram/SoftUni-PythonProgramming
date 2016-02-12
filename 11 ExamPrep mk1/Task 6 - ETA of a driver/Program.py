import sys
import csv


def main():
    path_to_file = input()
    result = 0.0
    with open(path_to_file) as f:
        reader = csv.reader(f)
        for row in reader:
            result += (float(row[1])-float(row[0])+1)/float(row[2])
    print("{:.2f}".format(result))


if __name__ == "__main__":
    sys.exit(main())