from multiprocessing import Process
from pymongo import MongoClient
import pandas as pd
import Levenshtein as lev
import threading

# MONGO DB CONNECTION
demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["BajajHacks"]

similarData = []
flag = 0


class Dedupe:

    def __init__(self, MRN, firstName, lastName, address, phone, exp, spez, edu):
        self.MRN_inp = MRN
        self.firstName_inp = firstName
        self.lastName_inp = lastName
        self.address_inp = address
        self.phone_inp = phone
        self.exp_inp = exp
        self.spez_inp = spez
        self.education_inp = edu

    def dedupe_eng(self, collectionName):
        myCollection = myDatabase[collectionName]

        # DECLARE THRESHOLDS HERE - INPUTS FROM SLIDERS IN FRONT END
        MRNThreshold = 0.8
        firstNameThreshold = 0.7
        lastNameThreshold = 0.7
        addressThreshold = 0.7
        phoneThreshold = 0.7
        expThreshold = 2
        spezThreshold = 0.7
        educationThreshold = 0.5

        # DEDUPE ALGORITHM
        for document in myCollection.find():
            score = 0

            MRNSimilarityScore = lev.ratio(document.get('MRN').lower(), self.MRN_inp)
            if MRNSimilarityScore >= MRNThreshold:
                score = score + 1

            firstNameSimilarityScore = lev.ratio(document.get('First Name').lower(), self.firstName_inp.lower())
            if firstNameSimilarityScore >= firstNameThreshold:
                score = score + 1

            lastNameSimilarityScore = lev.ratio(document.get('Last Name').lower(), self.lastName_inp.lower())
            if lastNameSimilarityScore >= lastNameThreshold:
                score = score + 1

            addressSimilarityScore = lev.ratio(document.get('Address'), self.address_inp)
            if addressSimilarityScore >= addressThreshold:
                score = score + 1

            phoneSimilarityScore = lev.ratio(str(document.get('phone')), self.phone_inp)
            if phoneSimilarityScore >= phoneThreshold:
                score = score + 1

            expSimilarityScore = abs(document.get('Years of Exp') - self.exp_inp)
            if expSimilarityScore >= expThreshold:
                score = score + 1

            spezSimilarityScore = lev.ratio(str(document.get('Specialization')), self.spez_inp)
            if spezSimilarityScore >= spezThreshold:
                score = score + 1

            eduSimilarityScore = lev.ratio(document.get('Education'), self.education_inp)
            if eduSimilarityScore >= educationThreshold:
                score = score + 1

            similarityScore = (MRNSimilarityScore + firstNameSimilarityScore + lastNameSimilarityScore +
                               addressSimilarityScore + phoneSimilarityScore + spezSimilarityScore +
                               eduSimilarityScore) / 7

            if score >= 5 or similarityScore > 0.60:
                global similarData
                similarData.append(
                    [document.get('MRN'), document.get('First Name'), document.get('Last Name'),
                     document.get('Address'),
                     str(document.get('Phone')), document.get('Specialization'), document.get('Years of Exp'),
                     document.get('Education'), similarityScore, collectionName])
                global flag
                flag = 1


def block1(obj):
    obj.dedupe_eng("Block1")


def block2(obj):
    obj.dedupe_eng("Block2")


def block3(obj):
    obj.dedupe_eng("Block3")


def block4(obj):
    obj.dedupe_eng("Block4")


def block5(obj):
    obj.dedupe_eng("Block5")


def block6(obj):
    obj.dedupe_eng("Block6")


def block7(obj):
    obj.dedupe_eng("Block7")


def block8(obj):
    obj.dedupe_eng("Block8")


def block9(obj):
    obj.dedupe_eng("Block9")


def block10(obj):
    obj.dedupe_eng("Block10")


if __name__ == '__main__':
    MRN_inp = input("Enter your MRN number: ")
    firstName_inp = input("Enter your First name: ")
    lastName_inp = input("Enter your Last name: ")
    address_inp = input("Enter your Address: ")
    phone_inp = input("Enter your Phone Number:")
    exp_inp = int(input("Enter your Years of Experience: "))
    spez_inp = input("Enter your Specialization: ")
    education_inp = input("Enter degrees earned: ")
    obj1 = Dedupe(MRN_inp, firstName_inp, lastName_inp, address_inp, phone_inp, exp_inp, spez_inp, education_inp)

    p1 = threading.Thread(target=block1, args=(obj1,))
    p1.start()

    p2 = threading.Thread(target=block2, args=(obj1,))
    p2.start()

    p3 = threading.Thread(target=block3, args=(obj1,))
    p3.start()

    p4 = threading.Thread(target=block4, args=(obj1,))
    p4.start()

    p5 = threading.Thread(target=block5, args=(obj1,))
    p5.start()

    p6 = threading.Thread(target=block6, args=(obj1,))
    p6.start()

    p7 = threading.Thread(target=block7, args=(obj1,))
    p7.start()

    p8 = threading.Thread(target=block8, args=(obj1,))
    p8.start()

    p9 = threading.Thread(target=block9, args=(obj1,))
    p9.start()

    p10 = threading.Thread(target=block10, args=(obj1,))
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

    count = 1
    if flag == 0:
        print('---Data unique. PROCEED TO ENTER THE DATA INTO THE DATASET/CSV  ---')
    else:
        print('--- SIMILAR ENTRIES FOUND ---')
        data_similarity = pd.DataFrame(similarData, columns=['MRN', 'FirstName', 'LastName', 'Address', 'Phone',
                                                             'Specialization', 'Years Of Exp', 'Education',
                                                             'SimilarityScore','Block Number'])
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
            print("Found in: ",row['Block Number'])
            print("")
            count = count + 1
            if count == 6:
                break

        print('-----PROCEED WITH HANDLING THE DUPLICATE ENTRIES ----- ')
    print('Finished.')