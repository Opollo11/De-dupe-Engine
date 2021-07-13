from pymongo import MongoClient
import pandas as pd


demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["MegaFileBajaj"]

myCollection = myDatabase["Existing CSV data"]

df = pd.read_csv('..\..\Database\Generated.csv')

# For Entering CSV rows into Mongo_DB
for index, row in df.iterrows():
    MRN = row['MRN Number']
    firstName=row['First Name']
    lastName = row['Last Name']
    address = row['Address']
    phone = row['Phone Number']
    yoe= row['Years of Exp.']
    specialization = row['Specialization']
    education = row['Education']
    myCollection.insert_many([{"MRN": MRN,
    "First Name": firstName,
    "Last Name": lastName, 
    "address": address, 
    "phone": phone, 
    "years of experience": yoe,
    "Specialization":specialization,
    "Education":education}])

print("Complete")
