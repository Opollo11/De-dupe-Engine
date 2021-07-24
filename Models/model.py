import numpy as np
import pandas as pd
import Levenshtein as lev
from csv import writer
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

df = pd.read_csv('..\Database\cleaned.csv')
data = []

name_inp = input("Enter the name: ")
phone_inp = input("Enter the phone number: ")
add_inp = input("Enter the address: ")
profId_inp = input("Enter the profile Id:")
uniqId_inp = input("Enter the unique Id: ")

# Declare Column Thresholds here - Will be fed from front end - alter accordingly
nameThreshold = 0.6
phoneThreshold = 0.7
addressThreshold = 0.5
profileIdThreshold = 0.5
uniqueIdThreshold = 0.5

flag = 0

for index, row in df.iterrows():
    score = 0

    nameSimilarityScore = lev.ratio(row['name'].lower(), name_inp.lower())
    if nameSimilarityScore >= nameThreshold:
        score = score + 1

    phoneSimilarityScore = lev.ratio(row['phone'], phone_inp)
    if phoneSimilarityScore >= phoneThreshold:
        score = score + 1

    addressSimilarityScore = lev.ratio(row['address'], add_inp)
    if addressSimilarityScore >= addressThreshold:
        score = score + 1

    profIdSimilarityScore = lev.ratio(row['profile_id'], profId_inp)
    if profIdSimilarityScore >= profileIdThreshold:
        score = score + 1

    uniqIdSimilarityScore = lev.ratio(row['uniq_id'], uniqId_inp)
    if uniqIdSimilarityScore >= uniqueIdThreshold:
        score = score + 1

    similarityScore = (nameSimilarityScore + phoneSimilarityScore + addressSimilarityScore + profIdSimilarityScore +
                       uniqIdSimilarityScore) / 5

    if score >= 3 or similarityScore > 0.65:
        # print('Entered Data was found to have a Similarity Score of :', similarityScore,
        #       ' with the following existing data -')
        # print(row)
        data.append([row['address'], row['name'], row['phone'], row['profile_id'], row['uniq_id'], similarityScore])
        flag = 1


count = 1

if flag == 0:
    print('---Data unique - PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
    row_contents = [0,add_inp, name_inp, phone_inp, profId_inp, uniqId_inp]
    # Appending a row to csv with missing entries
    append_list_as_row('cleaned.csv', row_contents)
else:
    print('---Similar Entries found--')
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
        if count == 5:
            break

    print('-----PROCEED WITH HANDLING THE DUPLICATE ENTRIES ----- ')
