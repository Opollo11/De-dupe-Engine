from pymongo import MongoClient
import Levenshtein as lev
import pandas as pd

# from fuzzywuzzy import fuzz as lev

demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["Finals"]
myCollection = myDatabase["10kRecord"]

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

flag = 0
data = []

# USER INPUTS - BULK
filename = input("Enter the file path/name: ")
df = pd.read_csv(filename)
for index, row in df.iterrows():
    mrn_inp = row['MRN Number']
    fname_inp = row['First Name']
    lname_inp = row['Last Name']
    dob_inp = row['DOB']
    phone_inp = str(row['Phone Number'])
    email_inp = row['Email']
    pincode_inp = str(row['Pincode'])
    state_inp = row['State']
    yoe_inp = str(row['Years of Exp'])
    spez_inp = row['Specialization']
    edu_inp = row['Education']

    maxSS = 0

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

        dobSimilarityScore = lev.ratio(document.get('DOB'), dob_inp)
        if dobSimilarityScore >= dobWeight:
            score = score + 1

        phoneSimilarityScore = lev.ratio(str(document.get('Phone Number')), phone_inp)
        if phoneSimilarityScore >= phoneWeight:
            score = score + 1

        emailSimilarityScore = lev.ratio(document.get('Email'), email_inp)
        if emailSimilarityScore >= emailWeight:
            score = score + 1

        pincodeSimilarityScore = lev.ratio(str(document.get('Pincode')), pincode_inp)
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

        tsimilarityScore = (mrnSimilarityScore * mrnWeight + fnameSimilarityScore * fnameWeight +
                           lnameSimilarityScore * lnameWeight + dobSimilarityScore * dobWeight +
                           phoneSimilarityScore * phoneWeight + emailSimilarityScore * emailWeight +
                           pincodeWeight * pincodeWeight + stateSimilarityScore * stateWeight + spezSimilarityScore * spezWeight +
                           eduSimilarityScore * eduWeight) / (
                                      mrnWeight + fnameWeight + lnameWeight + dobWeight + phoneWeight
                                      + emailWeight + pincodeWeight + stateWeight + spezWeight +
                                      eduWeight)
        if tsimilarityScore>maxSS:
            maxSS = tsimilarityScore

    if maxSS > 0.92:
        DUP = 'D'
        data.append(
            [mrn_inp, fname_inp, lname_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, yoe_inp, spez_inp,
             edu_inp, maxSS, DUP])
        maxSS = 0

    elif maxSS > 0.65:
        DUP = 'P'
        data.append(
            [mrn_inp, fname_inp, lname_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, yoe_inp, spez_inp,
             edu_inp, maxSS, DUP])
        maxSS = 0

    else:
        DUP = 'U'
        data.append(
            [mrn_inp, fname_inp, lname_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, yoe_inp, spez_inp,
             edu_inp, maxSS, DUP])
        maxSS = 0


data_summary = pd.DataFrame(data, columns=['MRN', 'First Name', 'Last Name', 'DOB', 'Phone Number', 'Email',
                                                  'Pincode', 'State', 'Years of Exp', 'Specialization', 'Education',
                                                  'SimilarityScore', 'DUP'])
data_summary.to_csv("Output.csv")
print("Output file generated. Check directory.")

# REPORT GENERATION - WRITING IT TO A FILE.
size = len(data_summary.index)
unique_count = (data_summary['DUP'].values == 'U').sum()
partial_count = (data_summary['DUP'].values == 'P').sum()
duplicate_count = (data_summary['DUP'].values == 'D').sum()
unique_count_perc = round(unique_count/size * 100, 2)
partial_count_perc = round(partial_count/size * 100, 2)
duplicate_count_perc = round(duplicate_count/size * 100, 2)
strlist = []
line1 = "--------Summary of Input Data----------\n"
line2 = "\n"
line3 = f"Total numbers of rows in the input data set: {size}."
line4 = f"\nUnique Entry Count: {unique_count} ({unique_count_perc} %)\n"
line5 = f"Duplicate Entry Count: {duplicate_count} ({duplicate_count_perc} %)\n"
line6 = f"Partial Similarity Entry Count: {partial_count} ({partial_count_perc} %)\n"
strlist = [line1, line2, line3, line4, line5, line6]

f= open("Report10k.txt", "w+")
for line in strlist:
    f.write(str(line))
print("Report Generated! Check file in directory")


