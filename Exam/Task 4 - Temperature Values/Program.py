import sys
import os
import csv
import collections
import iso8601


def main():
    try:
        temps_file = input()
        if not os.path.isfile(temps_file):
            raise InvalidInputException
        file_valid = False
        cities = set()
        dates = collections.OrderedDict()
        with open(temps_file, encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 0:
                    continue
                if "" in row:
                    raise InvalidInputException
                if len(row) != 3:
                    raise InvalidInputException
                if row[1] not in cities:
                    cities.add(row[1])
                try:
                    parsed_date = iso8601.parse_date(row[0])
                except:
                    raise InvalidInputException
                if parsed_date not in dates:
                    dates[parsed_date] = list()
                if row[1] in dates[parsed_date]:
                    raise InvalidInputException
                dates[parsed_date].append(row[1])

                file_valid = True
        if not file_valid:
            raise InvalidInputException
        is_data_complete = True
        for date in collections.OrderedDict(sorted(dates.items(), key=lambda t: t[0])):
            date_already_printed = False
            for city in sorted(cities):
                if city not in dates[date]:
                    if not date_already_printed:
                        #print_date = datetime.datetime(date.year, date.month, date.day)
                        #print(str(date.year) + '-' + str(date.month) + '-' + str(date.day), end="")
                        #print(date.isoformat(), end="")
                        #print(print_date.isoformat(), end="")
                        print(date.strftime('%Y-%m-%d'), end="")
                        date_already_printed = True
                    print("," + city, end="")
            if date_already_printed:
                is_data_complete = False
                print()
            if is_data_complete:
                print("ALL DATA AVAILABLE")
    except InvalidInputException:
        print("INVALID INPUT")


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
