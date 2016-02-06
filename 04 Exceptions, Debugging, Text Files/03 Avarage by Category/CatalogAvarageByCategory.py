import sys


def main():
    prices = {}
    counts = {}

    with open("../Common Resources/catalog_full.csv") as catalog_file:
        for line in catalog_file:
            values = line.split(sep=',')
            price = float(values[-1])
            category = values[-2]
            if category not in prices:
                prices[category] = 0
                counts[category] = 0
            prices[category] += price
            counts[category] += 1

    for entry in prices.keys():
        print(entry + ": " + str(prices[entry]/counts[entry]))


if __name__ == "__main__":
    sys.exit(main())