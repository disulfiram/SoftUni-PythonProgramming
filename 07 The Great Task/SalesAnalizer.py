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
        catalog = CatalogItem.parse_catalog(sys.argv[1])
        sales = SaleTransaction.parse_sales(sys.argv[2])
        print_analisys(catalog, sales)
    finally:
        pass


def print_analisys(catalog, sales):
    number_of_sales = len(sales)
    income = SaleTransaction.total_income(sales)
    print("Summary")
    print("-------")
    print("Total number of sales: {}".format(str(number_of_sales)))
    print("Total income: {}".format(str(income)))
    print("Average price per transaction: {}".format(str(income/number_of_sales)))
    print("Begin of data period: {}".format(SaleTransaction.begin_period(sales).isoformat()))
    print("End of data period: {}".format(SaleTransaction.end_period(sales).isoformat()))


if __name__ == "__main__":
    sys.exit(main())