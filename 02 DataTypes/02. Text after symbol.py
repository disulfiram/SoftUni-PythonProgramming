userInput = input()
character = input()

symbolIndex = userInput.find(character)
if symbolIndex != -1:
    print(userInput[symbolIndex + len(character):len(userInput)])
