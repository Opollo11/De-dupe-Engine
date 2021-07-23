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

    def __init__(self, MRN, firstName, lastName, dob, phone, email, pincode, state, exp, spez, edu):
        self.MRN_inp = MRN
        self.firstName_inp = firstName
        self.lastName_inp = lastName
        self.dob_inp = dob
        self.phone_inp = phone
        self.email_inp = email
        self.pincode_inp = pincode
        self.state_inp = state
        self.exp_inp = exp
        self.spez_inp = spez
        self.education_inp = edu

    def dedupe_eng(self, collectionName):
        myCollection = myDatabase[collectionName]

        # DECLARE THRESHOLDS HERE - INPUTS FROM SLIDERS IN FRONT END
        MRNThreshold = 90
        firstNameThreshold = 70
        lastNameThreshold = 70
        dobThreshold = 40
        phoneThreshold = 90
        emailThreshold = 50
        pincodeThreshold = 40
        stateThreshold = 60
        expThreshold = 70
        spezThreshold = 40
        educationThreshold = 40

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

            dobSimilarityScore = lev.ratio(document.get('DOB'), self.dob_inp)
            if dobSimilarityScore >= dobThreshold:
                score = score + 1

            phoneSimilarityScore = lev.ratio(str(document.get('Phone Number')), self.phone_inp)
            if phoneSimilarityScore >= phoneThreshold:
                score = score + 1

            emailSimilarityScore = lev.ratio(str(document.get('Email ID')), self.email_inp)
            if emailSimilarityScore >= emailThreshold:
                score = score + 1
            
            pincodeSimilarityScore = lev.ratio(str(document.get('Pincode')), self.pincode_inp)
            if pincodeSimilarityScore >= pincodeThreshold:
                score = score + 1

            stateSimilarityScore = lev.ratio(document.get('State').lower(), self.state_inp.lower())
            if stateSimilarityScore >= stateThreshold:
                score = score + 1

            #expSimilarityScore = lev.ratio(document.get('Experience'), self.exp_inp)
            # expSimilarityScore = abs(document.get('Years of Exp') - self.exp_inp)
            # if expSimilarityScore >= expThreshold:
            #     score = score + 1
            
            spezSimilarityScore = lev.ratio(document.get('Specialization').lower(), self.spez_inp.lower())
            if spezSimilarityScore >= spezThreshold:
                score = score + 1

            educationSimilarityScore = lev.ratio(document.get('Education').lower(), self.education_inp.lower())
            if educationSimilarityScore >= educationThreshold:
                score = score + 1
            

            # print(str(MRNSimilarityScore)+" " + str(firstNameSimilarityScore) + " " + str(lastNameSimilarityScore) + " " + str(dobSimilarityScore) + " " 
            # + str(phoneSimilarityScore) + " " + str(emailSimilarityScore) + " " + str(pincodeSimilarityScore) + " " + str(stateSimilarityScore) + " " + str(expSimilarityScore) 
            # + " " + str(spezSimilarityScore) + " " + str(educationSimilarityScore))
            similarityScore = (MRNSimilarityScore*MRNThreshold + firstNameSimilarityScore*firstNameThreshold + lastNameSimilarityScore*lastNameThreshold +
                               dobSimilarityScore*dobThreshold + phoneSimilarityScore*phoneThreshold + emailSimilarityScore*emailThreshold +
                               pincodeSimilarityScore*pincodeThreshold + stateSimilarityScore*stateThreshold + 
                               spezSimilarityScore*spezThreshold + educationSimilarityScore*educationThreshold) /  (MRNThreshold + firstNameThreshold + lastNameThreshold +
                                                                                                                            dobThreshold + phoneThreshold + emailThreshold +
                                                                                                                            pincodeThreshold + stateThreshold  +
                                                                                                                            spezThreshold + educationThreshold)
                               

            #similarityScore

            if score >= 5 or similarityScore > 0.60:
                global similarData
                similarData.append(
                    [document.get('MRN'), document.get('First Name'), document.get('Last Name'),
                     document.get('Date of Birth'), document.get('Phone Number'), document.get('Email ID'),
                     document.get('Pincode'), document.get('State'), document.get('Experience'),
                     document.get('Specialization'), document.get('Education'), similarityScore, collectionName])
                    
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
    dob_inp = input("Enter your date of birth: ")
    phone_inp = input("Enter your Phone Number: ")
    email_inp = input("Enter your Email: ")
    pincode_inp = input("Enter your Pincode: ")
    state_inp = input("Enter your State: ")
    exp_inp = int(input("Enter your Years of Experience: "))
    spez_inp = input("Enter your Specialization: ")
    education_inp = input("Enter degrees earned: ")
    obj1 = Dedupe(MRN_inp, firstName_inp, lastName_inp, dob_inp, phone_inp, email_inp, pincode_inp, state_inp, exp_inp, spez_inp, education_inp)

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
        data_similarity = pd.DataFrame(similarData, columns=['MRN', 'FirstName', 'LastName', 'DOB', 'Phone Number', 'Email', 'Pincode', 'State', 'Years Of Exp', 'Specialization', 'Education', 'SimilarityScore','Block Number'])
        data_similarity = data_similarity.sort_values('SimilarityScore', ascending=False)
        # THIS DATAFRAME CAN BE CONVERTED TO CSV FILE TOO IF NECESSARY
        for index, row in data_similarity.iterrows():
            print(count)
            print("SIMILARITY SCORE: ", row['SimilarityScore'])
            print("MRN: ", row['MRN'])
            print("Name: ", row['FirstName'], ' ', row['LastName'])
            print("DOB: ", row['DOB'])
            print("Phone: ", row['Phone Number'])
            print("Email: ", row['Email'])
            print("Pincode: ", row['Pincode'])
            print("State: ", row['State'])
            print("Experience: ", row['Years Of Exp'])
            print("Specialization: ", row['Specialization'])
            print("Education: ", row['Education'])
            print("Block Number: ", row['Block Number'])
            print("\n")
            count = count + 1
            if count == 6:
                break

        print('-----PROCEED WITH HANDLING THE DUPLICATE ENTRIES ----- ')
    print('Finished.')