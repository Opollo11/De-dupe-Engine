import random
setOfNumbers=list()
numLow=6000000000
numHigh=9999999999
while len(setOfNumbers) < 50000:
    setOfNumbers.append(random.randint(6000000000, 9999999999))

print(setOfNumbers)

