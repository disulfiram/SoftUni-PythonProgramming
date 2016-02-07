import os


for dirpath, dirnames, filenames in os.walk('./'):
    print("Директория '{}' съдържа:".format(dirpath))
    print("Под-директории: \n\t{}".format("\n\t".join(dirnames)))
    print("Файлове: \n\t{}".format("\n\t".join(filenames)))
    print("\n-------------\n\n")
