from multiprocessing import Process
from pymongo import MongoClient
import pandas as pd


# MONGO DB CONNECTION
demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["BajajHacks"]


def func1():
    for i in range(1, 10, 2):
        collection_name = "Block" + str(i)
        myCollection = myDatabase[collection_name]
        blockName = collection_name + ".csv"
        df = pd.read_csv(blockName)
        for index, row in df.iterrows():
            mrn = row['MRN Number']
            fname = row['First Name']
            lname = row['Last Name']
            address = row['Address']
            phone = row['Phone Number']
            yoe = row['Years of Exp.']
            spez = row['Specialization']
            edu = row['Education']
            myCollection.insert_many([{"MRN": mrn, "First Name": fname, "Last Name": lname, "Address": address,
                                       "phone": phone, "Specialization": spez, "Years of Exp": yoe,
                                       "Education": edu}])
        print("Block", i, "complete.")
    print("ODD blocks done")


def func2():
    for i in range(2, 11, 2):
        collection_name = "Block" + str(i)
        myCollection = myDatabase[collection_name]
        blockName = collection_name + ".csv"
        df = pd.read_csv(blockName)
        for index, row in df.iterrows():
            mrn = row['MRN Number']
            fname = row['First Name']
            lname = row['Last Name']
            address = row['Address']
            phone = row['Phone Number']
            yoe = row['Years of Exp.']
            spez = row['Specialization']
            edu = row['Education']
            myCollection.insert_many([{"MRN": mrn, "First Name": fname, "Last Name": lname, "Address": address,
                                       "phone": phone, "Specialization": spez, "Years of Exp": yoe,
                                       "Education": edu}])
        print("Block", i, "complete.")
    print("EVEN blocks done")


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
