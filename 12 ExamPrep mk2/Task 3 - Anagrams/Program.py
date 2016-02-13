import sys
import os


def main():
    try:
        words_file = input()
        if not os.path.isfile(words_file):
            raise InvalidInputException
        word = input()

        sorted_word = sorted(word)
        anagrams = list()
        with open(words_file, encoding="utf-8") as f:
            for row in f:
                if row.strip('\n') == word:
                    continue
                sorted_row = sorted(row.strip('\n'))
                if len(sorted_row) == len(sorted_word) and sorted_row == sorted_word:
                    anagrams.append(row)
        if len(anagrams) > 0:
            for anagram in sorted(anagrams):
                print(anagram, end='')
        else:
            print("NO ANAGRAMS")
    except InvalidInputException:
        print("INVALID INPUT")


class InvalidInputException(Exception):
    pass


if __name__ == "__main__":
    sys.exit(main())
