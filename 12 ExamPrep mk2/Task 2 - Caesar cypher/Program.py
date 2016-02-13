import sys


def main():
    try:
        key = int(input()) % 26
        message = input()
        if message.isspace() or message == "":
            raise Exception
        encrypted = encrypt_message(key, message)
        print(''.join(encrypted))
    except:
        print("INVALID INPUT")


def encrypt_message(key: int, message: str):
    result = list()
    for character in message:
        if ord('A') <= ord(character) <= ord('Z'):
            new_char = ord(character) + key
            if new_char > ord('Z'):
                new_char = ord('A') + new_char - ord('Z') - 1
            result.append(chr(new_char))
        elif character.isalpha():
            raise Exception
        else:
            result.append(character)
    return result


if __name__ == "__main__":
    sys.exit(main())
