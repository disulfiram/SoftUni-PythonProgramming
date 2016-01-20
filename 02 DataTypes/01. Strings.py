userInput = input()

if len(userInput) > 10:
    print(userInput[0:10] + '…')
else:
    print(userInput)