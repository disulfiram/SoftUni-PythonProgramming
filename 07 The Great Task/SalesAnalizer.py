import sys
import csv
from CatalogItem import CatalogItem


def main():
    if len(sys.argv) < 3:
        print("Usage: {} {{catalog csv file}} {{sales csv file}}".format(sys.argv[0]))
        return 0

    try:
        catalog = parse_catalog(sys.argv[1])
    finally:
        pass


def parse_catalog(catalogCSV):
    result = {}
    with open(catalogCSV) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            c = CatalogItem(row)
            result[c.id] = c
    return result


if __name__ == "__main__":
    sys.exit(main())