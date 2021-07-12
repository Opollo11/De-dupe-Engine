from pymongo import MongoClient
import pandas as pd


demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["BajajHacks"]

myCollection = myDatabase["Existing CSV data"]

df = pd.read_csv('cleaned.csv')

# For Entering CSV rows into Mongo_DB
for index, row in df.iterrows():
    name = row['name']
    address = row['address']
    phone = row['phone']
    profileID = row['profile_id']
    uniqueID = row['uniq_id']
    myCollection.insert_many([{"name": name, "address": address, "phone": phone, "profileID": profileID,
                               "uniqueID": uniqueID}])

print("Complete")
