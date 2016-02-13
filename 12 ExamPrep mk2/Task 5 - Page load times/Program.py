import sys
import re
from urllib.parse import urlparse


def main():
    data = input()
    pages = {}
    with open(data, encoding="utf-8") as f:
        for row in f:
            url_pattern = re.compile('(?<=url=")([^\s]*)(?=\")')
            url_match = url_pattern.search(row)
            url = urlparse(url_match.group())
            if not url.path.endswith('/ws/'):
                if url.path not in pages:
                    pages[url.path] = [0,0]
                time_pattern = re.compile('(?<=resp_t=")([^\s]*)(?=\")')
                time_match = time_pattern.search(row)
                time = time_match.group()
                pages[url.path][0] += float(time)
                pages[url.path][1] += 1

    max_average = 0.0
    max_page = ""
    for page in pages:
        average = pages[page][0]/pages[page][1]
        if average > max_average:
            max_average = average
            max_page = page

    print(max_page)
    print("{:.3f}".format(max_average))

class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
