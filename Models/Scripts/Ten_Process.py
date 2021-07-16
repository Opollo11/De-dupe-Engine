from multiprocessing import Process
from pymongo import MongoClient
import pandas as pd
import Levenshtein as lev

# MONGO DB CONNECTION
demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["BajajHacks"]

similarData = []
flag = 0

# SEARCH RESPECTIVE COLLECTION IN MONGO -
def dedupe(collectionName, MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
           education_inp):
    myCollection = myDatabase[collectionName]

    # DECLARE THRESHOLDS HERE - INPUTS FROM SLIDERS IN FRONT END
    MRNThreshold = 0.8
    firstNameThreshold = 0.7
    lastNameThreshold = 0.7
    addressThreshold = 0.5
    phoneThreshold = 0.7
    expThreshold = 2
    spezThreshold = 0.7
    educationThreshold = 0.5

    # # USER INPUT - SINGLE USER SCENARIO - FED FROM FORMS IN FRONTEND
    # MRN_inp = input("Enter your MRN number: ")
    # firstName_inp = input("Enter your First name: ")
    # lastName_inp = input("Enter your Last name: ")
    # address_inp = input("Enter your Address: ")
    # phone_inp = input("Enter your Phone Number:")
    # exp_inp = input("Enter your Years of Experience: ")
    # spez_inp = input("Enter your Specialization: ")
    # education_inp = input("Enter degrees earned: ")

    # DEDUPE ALGORITHM
    for document in myCollection.find():
        score = 0

        MRNSimilarityScore = lev.ratio(document.get('MRN').lower(), MRN_inp)
        if MRNSimilarityScore >= MRNThreshold:
            score = score + 1

        firstNameSimilarityScore = lev.ratio(document.get('First Name').lower(), firstName_inp.lower())
        if firstNameSimilarityScore >= firstNameThreshold:
            score = score + 1

        lastNameSimilarityScore = lev.ratio(document.get('Last Name').lower(), lastName_inp.lower())
        if lastNameSimilarityScore >= lastNameThreshold:
            score = score + 1

        addressSimilarityScore = lev.ratio(document.get('Address'), address_inp)
        if addressSimilarityScore >= addressThreshold:
            score = score + 1

        phoneSimilarityScore = lev.ratio(str(document.get('phone')), phone_inp)
        if phoneSimilarityScore >= phoneThreshold:
            score = score + 1

        expSimilarityScore = abs(document.get('Years of Exp') - exp_inp)
        if expSimilarityScore >= expThreshold:
            score = score + 1

        spezSimilarityScore = lev.ratio(str(document.get('Specialization')), spez_inp)
        if spezSimilarityScore >= spezThreshold:
            score = score + 1

        eduSimilarityScore = lev.ratio(document.get('Education'), education_inp)
        if eduSimilarityScore >= educationThreshold:
            score = score + 1

        similarityScore = (MRNSimilarityScore + firstNameSimilarityScore + lastNameSimilarityScore +
                           addressSimilarityScore + phoneSimilarityScore + spezSimilarityScore +
                           eduSimilarityScore) / 7

        if score >= 5 or similarityScore > 0.65:
            similarData.append(
                [document.get('MRN'), document.get('First Name'), document.get('Last Name'), document.get('Address'),
                 str(document.get('Phone')), document.get('Specialization'), document.get('Years of Exp'),
                 document.get('Education'), similarityScore, collectionName])
            global flag
            flag = 1

    count = 1

    if flag == 0:
        print('---Data unique. No Similar Entries in', collectionName,
              '- PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
    else:
        print('--- SIMILAR ENTRIES FOUND in ', collectionName, '---')
        data_similarity = pd.DataFrame(similarData, columns=['MRN', 'FirstName', 'LastName', 'Address', 'Phone',
                                                             'Specialization', 'Years Of Exp', 'Education',
                                                             'SimilarityScore'])
        data_similarity = data_similarity.sort_values('SimilarityScore', ascending=False)
        # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
        for index, row in data_similarity.iterrows():
            print(count)
            print("SIMILARITY SCORE: ", row['SimilarityScore'])
            print("MRN: ", row['MRN'])
            print("Name: ", row['FirstName'], ' ', row['LastName'])
            print("Address: ", row['Address'])
            print("Phone: ", row['Phone'])
            print("Years of Exp: ", row['Years Of Exp'])
            print("Specialization: ", row['Specialization'])
            print('Education: ', row['Education'])
            print("")
            count = count + 1
            if count == 6:
                break

        print('-----PROCEED WITH HANDLING THE DUPLICATE ENTRIES ----- ')


def block1(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block1'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block2(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block2'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block3(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block3'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block4(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block4'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block5(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block5'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block6(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block6'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block7(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block7'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block8(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block8'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block9(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block9'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


def block10(MRN, fname, lname, address, phone, exp, spez, edu):
    collectionName = 'Block10'
    dedupe(collectionName, MRN, fname, lname, address, phone, exp, spez, edu)


if __name__ == '__main__':
    # USER INPUT - SINGLE USER SCENARIO - FED FROM FORMS IN FRONTEND
    MRN_inp = input("Enter your MRN number: ")
    firstName_inp = input("Enter your First name: ")
    lastName_inp = input("Enter your Last name: ")
    address_inp = input("Enter your Address: ")
    phone_inp = input("Enter your Phone Number:")
    exp_inp = int(input("Enter your Years of Experience: "))
    spez_inp = input("Enter your Specialization: ")
    education_inp = input("Enter degrees earned: ")

    p1 = Process(target=block1, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                               education_inp))
    p1.start()

    p2 = Process(target=block2, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                               education_inp))
    p2.start()

    p3 = Process(target=block3, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p3.start()

    p4 = Process(target=block4, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p4.start()

    p5 = Process(target=block5, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p5.start()

    p6 = Process(target=block6, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p6.start()

    p7 = Process(target=block7, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p7.start()

    p8 = Process(target=block8, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p8.start()

    p9 = Process(target=block9, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p9.start()

    p10 = Process(target=block10, args=(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp,
                                      education_inp))
    p10.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()

    # count = 1
    # if bool(similarData):
    #     print('---Data unique. PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
    # else:
    #     print('--- SIMILAR ENTRIES FOUND ---')
    #     data_similarity = pd.DataFrame(similarData, columns=['MRN', 'FirstName', 'LastName', 'Address', 'Phone',
    #                                                          'Specialization', 'Years Of Exp', 'Education',
    #                                                          'SimilarityScore','Block Number'])
    #     data_similarity = data_similarity.sort_values('SimilarityScore', ascending=False)
    #     # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
    #     for index, row in data_similarity.iterrows():
    #         print(count)
    #         print("SIMILARITY SCORE: ", row['SimilarityScore'])
    #         print("MRN: ", row['MRN'])
    #         print("Name: ", row['FirstName'], ' ', row['LastName'])
    #         print("Address: ", row['Address'])
    #         print("Phone: ", row['Phone'])
    #         print("Years of Exp: ", row['Years Of Exp'])
    #         print("Specialization: ", row['Specialization'])
    #         print('Education: ', row['Education'])
    #         print("Found in: ",row['Block Number'])
    #         print("")
    #         count = count + 1
    #         if count == 6:
    #             break
    #
    #     print('-----PROCEED WITH HANDLING THE DUPLICATE ENTRIES ----- ')
    print('Finished.')
