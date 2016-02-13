import sys
import collections


def main():
    box_sides = list()
    for n in range(3):
        box_sides.append(float(input()))
    box_sides.sort(reverse=True)
    medicine_file = input()
    medicine = parse_medicine(medicine_file)
    medicine
    for med in medicine:
        is_OK = True
        for side in range(3):
            temp = float(medicine[med][side])
            if box_sides[side] < float(medicine[med][side]):
                is_OK = False
                break
        if is_OK:
            print(med)


def parse_medicine(file):
    result = collections.OrderedDict()
    with open(file, encoding="utf-8") as f:
        for row in f:
            values = row.split(sep=',')
            dimensions = values[1:4]
            dimensions.sort(reverse=True)
            result[values[0]] = dimensions
    return result


if __name__ == "__main__":
    sys.exit(main())
