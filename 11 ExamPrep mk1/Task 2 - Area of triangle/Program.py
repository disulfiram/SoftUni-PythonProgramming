import sys
import math


def main():
    a = 0.0
    b = 0.0
    c = 0.0
    try:
        a = float(input())
        b = float(input())
        c = float(input())
    except:
        print("INVALID INPUT")
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if s == 0:
        print()
        return 0
    print("{:.2f}".format(s))


if __name__ == "__main__":
    sys.exit(main())