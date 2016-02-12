import iso8601
import csv
import datetime
import pytz


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
            self.datetime = iso8601.parse_date(arguments[3])
            self.price = float(arguments[4])

    def parse_sales(salesCSV):
        result = list()
        with open(salesCSV) as f:
            reader = csv.reader(f)
            for row in reader:
                result.append(SaleTransaction(row))
        return result

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