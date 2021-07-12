from pymongo import MongoClient
import Levenshtein as lev
import pandas as pd

demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["BajajHacks"]
myCollection = myDatabase["Existing CSV data"]

# DECLARE THRESHOLDS -  SLIDER CONCEPT IN UI
nameThreshold = 0.6
phoneThreshold = 0.7
addressThreshold = 0.5
profileIdThreshold = 0.5
uniqueIdThreshold = 0.5

# USER INPUTS - SINGLE CUSTOMER SCENARIO
name_inp = input("Enter the name: ")
phone_inp = input("Enter the phone number: ")
add_inp = input("Enter the address: ")
profId_inp = input("Enter the profile Id:")
uniqId_inp = input("Enter the unique Id: ")

flag = 0
data = []
for document in myCollection.find():
    score = 0

    nameSimilarityScore = lev.ratio(document.get('name').lower(), name_inp.lower())
    if nameSimilarityScore >= nameThreshold:
        score = score + 1

    phoneSimilarityScore = lev.ratio(document.get('phone'), phone_inp)
    if phoneSimilarityScore >= phoneThreshold:
        score = score + 1

    addressSimilarityScore = lev.ratio(document.get('address'), add_inp)
    if addressSimilarityScore >= addressThreshold:
        score = score + 1

    profIdSimilarityScore = lev.ratio(document.get('profileID'), profId_inp)
    if profIdSimilarityScore >= profileIdThreshold:
        score = score + 1

    uniqIdSimilarityScore = lev.ratio(document.get('uniqueID'), uniqId_inp)
    if uniqIdSimilarityScore >= uniqueIdThreshold:
        score = score + 1

    similarityScore = (nameSimilarityScore + phoneSimilarityScore + addressSimilarityScore + profIdSimilarityScore +
                       uniqIdSimilarityScore) / 5

    if score >= 4 or similarityScore > 0.65:
        data.append([document.get('address'), document.get('name'), document.get('phone'), document.get('profileID'),
                     document.get('uniqueID'), similarityScore])
        flag = 1

count = 1

if flag == 0:
    print('---Data unique - PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
else:
    print('--- SIMILAR ENTRIES FOUND ---')
    data_similarity = pd.DataFrame(data, columns=['Address', 'Name', 'Phone', 'ProfileId', 'UniqueId',
                                                  'SimilarityScore'])
    data_similarity = data_similarity.sort_values('SimilarityScore', ascending=False)
    # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
    for index, row in data_similarity.iterrows():
        print(count)
        print("SIMILARITY SCORE: ", row['SimilarityScore'])
        print("Name: ", row['Name'])
        print("Address: ", row['Address'])
        print("Phone: ", row['Phone'])
        print("Profile ID: ", row['ProfileId'])
        print("Unique ID: ", row["UniqueId"])
        print("")
        count = count + 1
        if count == 6:
            break

    print('-----PROCEED WITH HANDLING THE DUPLICATE ENTRIES ----- ')