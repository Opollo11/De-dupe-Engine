import random
import csv
setOfNumbers=list()
yearsOfExperience=list()
numLow=6000000000
numHigh=9999999999
while len(setOfNumbers) < 100000:
    setOfNumbers.append(random.randint(6000000000, 9999999999))
    yearsOfExperience.append(random.randint(1, 30))

#print(setOfNumbers)
filename = "..\..\Database\MobileNumber.csv"
numbers= list();
check=list()
for i in range(1,100000):#setOfNumbers,yearsOfExperience:
    check=list()
    check.append(setOfNumbers[i])
    check.append(yearsOfExperience[i])
    numbers.append(check)
with open(filename, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(['Phone Number','Years Of Experience']) 
    csvwriter.writerows(numbers)




