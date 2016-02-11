import iso8601


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
