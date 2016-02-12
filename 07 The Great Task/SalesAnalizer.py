import sys
import csv
import iso8601
import datetime
import pytz
from CatalogItem import CatalogItem
from SaleTransaction import SaleTransaction


def main():
    if len(sys.argv) < 3:
        print("Usage: {} {{catalog csv file}} {{sales csv file}}".format(sys.argv[0]))
        return 0

    try:
        catalog = parse_catalog(sys.argv[1])
        sales = parse_sales(sys.argv[2])
        print_analisys(catalog, sales)
    finally:
        pass


def print_analisys(catalog, sales):
    number_of_sales = len(sales)
    income = total_income(sales)
    print("Summary")
    print("-------")
    print("Total number of sales: {}".format(str(number_of_sales)))
    print("Total income: {}".format(str(income)))
    print("Average price per transaction: {}".format(str(income/number_of_sales)))
    print("Begin of data period: {}".format(begin_period(sales).isoformat()))
    print("End of data period: {}".format(end_period(sales).isoformat()))


def end_period(sales):
    result = datetime.datetime.min
    result = result.replace(tzinfo=pytz.timezone('Europe/Sofia'))
    for sale in sales:
        if sale.datetime > result:
            result = sale.datetime
    return result


def begin_period(sales):
    result = datetime.datetime.max
    result = result.replace(tzinfo=pytz.timezone('Europe/Sofia'))
    for sale in sales:
        if sale.datetime < result:
            result = sale.datetime
    return result


def total_income(sales):
    result = float()
    for sale in sales:
        result += sale.price
    return result


def parse_sales(salesCSV):
    result = list()
    with open(salesCSV) as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(SaleTransaction(row))
    return result


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