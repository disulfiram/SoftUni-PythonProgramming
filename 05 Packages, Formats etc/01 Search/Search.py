import os
import sys


def main():
    file = sys.argv[1]
    location = sys.argv[2]
    file_found = False
    if os.path.exists(location):
        file_found = check_files(file, location)
    else:
        print("Directory nod found.")
    if not file_found:
        print("File \"" + file + "\" not found")


def check_files(file, loc, file_found=False):
    for root, dirs, files in os.walk(loc):
        for directory in dirs:
            file_found = check_files(file, directory, file_found)
        for name in files:
            if name == file:
                print(os.path.join(root, name))
                file_found = True
    return file_found


if __name__ == "__main__":
    sys.exit(main())
