from pymongo import MongoClient
import Levenshtein as lev
import pandas as pd
# from fuzzywuzzy import fuzz as lev

demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["Finals"]
myCollection = myDatabase["100kRecord"]

# DECLARE THRESHOLDS -  SLIDER CONCEPT IN UI
mrnWeight = 0.8
fnameWeight = 0.6
lnameWeight = 0.6
dobWeight = 0.65
phoneWeight = 0.7
emailWeight = 0.65
pincodeWeight = 0.5
stateWeight = 0.5
# yoeWeight = 0.5
spezWeight = 0.65
eduWeight = 0.6

# USER INPUTS - SINGLE CUSTOMER SCENARIO
mrn_inp = input("Enter MRN number")
fname_inp = input("Enter first name: ")
lname_inp = input("Enter last name: ")
dob_inp = input("DOB(dd-mm-yyyy): ")
phone_inp = input("Enter phone number: ")
email_inp = input("Enter email address: ")
pincode_inp = input("Enter the Pincode: ")
state_inp = input("Enter the State:")
yoe_inp = input("Enter the Years of Experience:  ")
spez_inp = input("Enter the Specialization: ")
edu_inp = input("Enter the Education(Degrees): ")

flag = 0
data = []
for document in myCollection.find():
    score = 0

    mrnSimilarityScore = lev.ratio(document.get('MRN').lower(), mrn_inp.lower())
    if mrnSimilarityScore >= mrnWeight:
        score = score + 1

    fnameSimilarityScore = lev.ratio(document.get('First Name').lower(), fname_inp.lower())
    if fnameSimilarityScore >= fnameWeight:
        score = score + 1

    lnameSimilarityScore = lev.ratio(document.get('Last Name').lower(), lname_inp.lower())
    if lnameSimilarityScore >= lnameWeight:
        score = score + 1

    dobSimilarityScore = lev.ratio(document.get('DOB'),dob_inp)
    if dobSimilarityScore >= dobWeight:
        score = score + 1

    phoneSimilarityScore = lev.ratio(str(document.get('Phone Number')), phone_inp)
    if phoneSimilarityScore >= phoneWeight:
        score = score + 1

    emailSimilarityScore = lev.ratio(document.get('Email'), email_inp)
    if emailSimilarityScore >= emailWeight:
        score = score + 1

    pincodeSimilarityScore = lev.ratio(str(document.get('Pincode')),pincode_inp)
    if pincodeSimilarityScore >= pincodeWeight:
        score = score + 1

    stateSimilarityScore = lev.ratio(document.get('State'), state_inp)
    if stateSimilarityScore >= stateWeight:
        score = score + 1

    spezSimilarityScore = lev.ratio(document.get('Specialization'), spez_inp)
    if spezSimilarityScore >= spezWeight:
        score = score + 1

    eduSimilarityScore = lev.ratio(document.get('Education'), edu_inp)
    if spezSimilarityScore >= spezWeight:
        score = score + 1

    similarityScore = (mrnSimilarityScore*mrnWeight + fnameSimilarityScore*fnameWeight +
                       lnameSimilarityScore*lnameWeight + dobSimilarityScore*dobWeight +
                       phoneSimilarityScore*phoneWeight + emailSimilarityScore*emailWeight +
                       pincodeWeight*pincodeWeight + stateSimilarityScore*stateWeight + spezSimilarityScore*spezWeight +
                       eduSimilarityScore*eduWeight) / (mrnWeight + fnameWeight + lnameWeight + dobWeight + phoneWeight
                                                        + emailWeight + pincodeWeight + stateWeight + spezWeight +
                                                        eduWeight)


    if score >= 8 or similarityScore > 0.75:
        data.append([document.get('MRN'), document.get('First Name'), document.get('Last Name'), document.get('DOB'),
                     document.get('Phone Number'), document.get('Email'), document.get('Pincode'), document.get('State'),
                     document.get('Years of Exp'), document.get('Specialization'), document.get('Education'),
                     similarityScore])
        flag = 1

count = 1
if flag == 0:
    print('---Data unique - PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
else:
    print('--- SIMILAR ENTRIES FOUND ---')
    data_similarity = pd.DataFrame(data, columns=['MRN', 'First Name', 'Last Name', 'DOB', 'Phone Number', 'Email',
                                                  'Pincode', 'State', 'Years of Exp', 'Specialization', 'Education',
                                                  'SimilarityScore'])

    data_similarity = data_similarity.sort_values('SimilarityScore', ascending=False)
    # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
    for index, row in data_similarity.iterrows():
        print(count)
        print("SIMILARITY SCORE: ", row['SimilarityScore'])
        print("MRN : ", row["MRN"])
        print("Name: ", row['First Name']+' '+row['Last Name'])
        print("DOB: ", row['DOB'])
        print("Phone: ", row['Phone Number'])
        print("Email ID: ", row['Email'])
        print("Pincode: ", row["Pincode"])
        print("State: ", row["State"])
        print("Years of Exp.: ", row["Years of Exp"])
        print("Specialization : ", row["Specialization"])
        print("Education: ", row["Education"])
        print("")
        count = count + 1
        if count == 6:
            break
    data_similarity.to_csv("SimilarData_SingleRowInput.csv")

