import sys


def main():
    item = input()
    file_location = input()
    sales = parse_sales(file_location)
    min_price = sys.float_info.max
    city = ""
    for sale in sales:
        if sale[0].strip('\"') == item and float(sale[-1]) < min_price:
            min_price = float(sale[-1])
            city = sale[2].strip('\"')
    print(city)


def parse_sales(file_location):
    result = list()
    with open(file_location, encoding='utf-8') as f:
        for row in f:
            values = row.strip('\n').split(sep=',')
            result.append(values)
    return result


if __name__ == "__main__":
    sys.exit(main())
