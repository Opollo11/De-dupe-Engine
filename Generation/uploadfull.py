
from pymongo import MongoClient
import pandas as pd

# MONGO DB CONNECTION
demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["Finals"]
collection_name = "100kRecord"
myCollection = myDatabase[collection_name]
df = pd.read_csv("D:\Finals\Generation\Generated100k.csv")
for index, row in df.iterrows():
    mrn = row['MRN Number']
    fname = row['First Name']
    lname = row['Last Name']
    dob = row['DOB']
    phone = row['Phone Number']
    emailid = row['Email']
    pincode = row['Pincode']
    state = row['State']
    yoe = row['Years of Exp']
    spez = row['Specialization']
    edu = row['Education']
    myCollection.insert_many([{"MRN": mrn, "First Name": fname, "Last Name": lname, "DOB": dob,
                               "Phone Number": phone, "Email": emailid, "Pincode": pincode, "State": state,
                               "Years of Exp": yoe, "Specialization": spez,
                               "Education": edu}])
print("Done")
 
