import sys
import csv


def main():
    fridge_temps = input()
    fridge_data = list()
    with open(fridge_temps) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            fridge_data.append([row[0], float(row[1])])
    previous_temp = float("inf")
    for dt in fridge_data:
        if (dt[1] - previous_temp) > 4:
            print(dt[0])
        previous_temp = dt[1]


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
