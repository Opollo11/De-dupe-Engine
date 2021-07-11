import csv
from fuzzywuzzy import process
filename = "cleaned.csv"
#implementing the fuzzywuzzy library and checking out outputs

fields = []
rows = []
  
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
      
    # extracting field names through first row
    fields = next(csvreader)
  
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
  
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
  
# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
  
#  printing first 5 rows
print('\nFirst 5 rows are:\n')
names=[]
address=[]
phone=[]
for row in rows:
    # parsing each column of a row
    for col in row[2:3]:
        names.append(col)
    for col in row[1:2]:
        address.append(col)
    for col in row[3:4]:
        phone.append(col)

print(len(names))

queryName=input("Enter the name of the doctor :")
queryAddress= input("\n Enter your address :")
queryPhone= input("\n Enter your phone number :")



resultsName=process.extract(queryName, names, limit=10)

resultsAddress=process.extract(queryAddress, address, limit=10)
resultsPhone=process.extract(queryPhone, phone,limit=10)


print("\n")
print(resultsName)
print("\n")
print(resultsAddress)
print("\n")
print(resultsPhone)

NameWeight=int(input("Enter the weight to be given for Name (out of 100) : "))
AddressWeight=int(input("Enter the weight to be given for Address (out of 100) : "))
PhoneWeight=int(input("Enter the weight to be given for Phone (out of 100) : "))

total=[]
total.append((resultsName[0][1]*(NameWeight/100) + resultsAddress[0][1]*(AddressWeight/100) + resultsPhone[0][1]*(PhoneWeight/1000))/3)

print("\n The total confidence of the persons data is : ", total)