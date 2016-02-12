import sys


def main():
    exchange_rate_path = input()
    amounts_path = input()
    exchange_rates = parse_exchange(exchange_rate_path)
    amounts = parse_amounts(amounts_path)
    for amount in amounts:
        print("{:.2f}".format(float(amount[0]) / exchange_rates[amount[1]]))


def parse_amounts(file_path):
    result = list()
    with open(file_path, encoding="utf-8") as f:
        for row in f:
            values = row.strip().split(sep=' ')
            result.append(values)
    return result


def parse_exchange(file_path):
    result = {}
    with open(file_path, encoding="utf-8") as f:
        for row in f:
            values = row.split(sep=' ')
            if values[0] not in result:
                result[values[0]] = float(values[1])
            else:
                print("Duplicate values")
    return result


if __name__ == "__main__":
    sys.exit(main())
