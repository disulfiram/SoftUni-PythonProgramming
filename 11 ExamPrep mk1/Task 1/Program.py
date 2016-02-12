import sys


def main():
    string = input()
    symbols = {}
    if string.isspace() or not string.whitespace():
        for symbol in string:
            if symbol not in symbols:
                symbols[symbol] = 0
            symbols[symbol] += 1
        max_symbol = list(symbols.keys())[0]
        for symbol in symbols:
            if symbols[symbol] > symbols[max_symbol]:
                max_symbol = symbol
        print(max_symbol)
    else:
        print("INVALID INPUT")


if __name__ == "__main__":
    sys.exit(main())