from pymongo import MongoClient
import pandas as pd
import Levenshtein as lev

simi=list()
# MONGO DB CONNECTION
demoClient = MongoClient()
myClient = MongoClient("localhost", 27017)
myDatabase = myClient["MegaFileBajaj"]

MRN_inp = input("Enter your MRN number: ")
firstName_inp = input("Enter your First name: ")
lastName_inp = input("Enter your Last name: ")
address_inp = input("Enter your Address: ")
phone_inp = input("Enter your Phone Number:")
exp_inp = int(input("Enter your Years of Experience: "))
spez_inp = input("Enter your Specialization: ")
education_inp = input("Enter degrees earned: ")


collectionName ="Existing CSV data"
myCollection = myDatabase[collectionName]


MRNThreshold = 0.8
firstNameThreshold = 0.7
lastNameThreshold = 0.7
addressThreshold = 0.5
phoneThreshold = 0.7
expThreshold = 2
spezThreshold = 0.7
educationThreshold = 0.5

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

    addressSimilarityScore = lev.ratio(document.get('address'), address_inp)
    if addressSimilarityScore >= addressThreshold:
        score = score + 1

    phoneSimilarityScore = lev.ratio(str(document.get('phone')), phone_inp)
    if phoneSimilarityScore >= phoneThreshold:
        score = score + 1

    expSimilarityScore = abs(document.get('years of experience') - exp_inp)
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
        print([document.get('MRN'), document.get('First Name'), document.get('Last Name'), document.get('Address'),
                 str(document.get('Phone')), document.get('Specialization'), document.get('Years of Exp'),
                 document.get('Education'), similarityScore])


