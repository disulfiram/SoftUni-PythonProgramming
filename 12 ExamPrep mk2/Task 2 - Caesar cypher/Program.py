import sys


def main():
    key = 0
    try:
        key = int(input())
    except:
        print("INVALID INPUT")
    message = input()
    encripted = encript_message(key, message)
    print(''.join(encripted))


def encript_message(key, message):
    result = list()

    for character in message:
        if ord(character) >= ord('A') and ord(character) <= ord('Z'):
            new_char = ord(character) + key
            if new_char > ord('Z'):
                new_char = ord('A') + new_char - ord('Z') - 1
            result.append(chr(new_char))
        else:
            result.append(character)
    return result


if __name__ == "__main__":
    sys.exit(main())