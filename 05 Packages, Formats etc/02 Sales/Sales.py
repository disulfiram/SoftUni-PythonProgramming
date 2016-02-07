import sys
from datetime import datetime


def main():
    sales_by_dates = {}

    with open("sales.csv") as sales:
        for line in sales:
            values = line.split(sep=',')
            date = datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S")
            price = float(values[1])
            if date.date() not in sales_by_dates:
                sales_by_dates[date.date()] = 0
            sales_by_dates[date.date()] += price

    min = float("inf")
    min_date = datetime.now()
    max = 0
    max_date = datetime.now()

    for date in sales_by_dates:
        if sales_by_dates[date] > max:
            max = sales_by_dates[date]
            max_date = date
        if sales_by_dates[date] < min:
            min = sales_by_dates[date]
            min_date = date

    print("Date with maximum sales is: " + str(max_date) + " with " + str(sales_by_dates[max_date]))
    print("Date with minimum sales is: " + str(min_date) + " with " + str(sales_by_dates[min_date]))

if __name__ == "__main__":
    sys.exit(main())