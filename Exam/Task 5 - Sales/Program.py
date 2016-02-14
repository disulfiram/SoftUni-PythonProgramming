import sys
import csv
import os
from collections import OrderedDict


def main():
    try:
        sales_file = input()
        if not os.path.isfile(sales_file):
            raise InvalidInputException
        items_sold = SaleTransaction.parse_sales(sales_file)

        has_unique_items = False
        for city in sorted(items_sold):
            unique_items = list()
            for item in items_sold[city]:
                item_unique = True
                for city2 in items_sold:
                    if city != city2:
                        if item in items_sold[city2]:
                            item_unique = False
                if item_unique:
                    unique_items.append(item)
            if len(unique_items) > 0:
                has_unique_items = True
                print(city,end="")
                for item in sorted(unique_items):
                    print(","+item,end="")
                print()
        if not has_unique_items:
            print("NO UNIQUE SALES")

    except InvalidInputException:
        print("INVALID INPUT")


class SaleTransaction:
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.id = kwargs["id"]
            self.country = kwargs["country"]
            self.city = kwargs["city"]
            self.datetime = kwargs["datetime"]
            self.price = kwargs["price"]
        elif len(args) > 0:
            arguments = args[0]
            self.id = arguments[0]
            self.country = arguments[1]
            self.city = arguments[2]

    def parse_sales(salesCSV):
        result = OrderedDict()
        with open(salesCSV) as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 0:
                    continue
                if "" in row:
                    raise InvalidInputException
                if row[2] not in result:
                    result[row[2]] = set()
                result[row[2]].add(row[0])
        return result


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
