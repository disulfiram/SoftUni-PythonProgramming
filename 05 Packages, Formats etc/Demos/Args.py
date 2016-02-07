import sys
print("Параметри на програмата:")
print(sys.argv)
for idx, a in enumerate(sys.argv):
    print("Argument #{} - '{}'".format(idx, a))