userInput = input("Start with the prices")
prices = []
while (userInput != "stop"):
    prices.append(userInput)
    userInput = input()

prices = map(int, prices)
prices.sort()
lowest = prices[0]
del prices[0]
biggest = prices[-1]
del prices[-1]

sum = 0
for number in prices:
    sum = sum + number

avg = sum/len(prices)

print(lowest)
print(biggest)
print(avg)