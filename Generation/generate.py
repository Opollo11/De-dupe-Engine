import numpy as np
import pandas as pd
import random
import names
import string
from faker import Faker
import time
import datetime
from random import randint
import math


# PHONE NUMBER GENERATION
def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}{}{}'.format(first, second, last)


# GENERATING RANDOM YEARS OF EXPERIENCE
def assignYOE():
    yoe = random.randint(3, 25)
    return yoe


# FIRSTNAME AND LASTNAME GENERATION
def getName():
    name = names.get_full_name()
    return name


# SPECIALIZATION GENERATION
def getSpecialization(x):
    splist = ['General Physician, ', 'Gynaecologist, ', 'Orthopedic, ', 'Dermatologist, ', 'ENT, ', 'Sexologist, ',
              'Ophthalmologist, ', 'Paediatrician, ', 'Urologist, ', 'Dentist, ', 'Physiotherapist, ', 'Psychiatrist, ']
    str = ''
    for i in range(0, x):
        index = random.randint(0, 11)
        if str.find(splist[index]) == -1:
            str = str + splist[index]
    return str


# EDUCATION GENERATION
def getEducation():
    edlist = ['MD in Anatomy, ', 'MD in Anesthesia, ', 'MD in Aerospace Medicine, ', 'MD in Biochemistry, ',
              'MD in Dermatology, ', 'MD in ENT, ', 'MD in Forensic Medicine, ', 'MD in Geriatrics, ',
              'MD in General Surgery, ', 'MD in Ophthalmology, ',
              'MD in Obstetrics & Gynecology, ', 'MD in Orthopedics, ', 'MS Pediatric surgery, ',
              'MS Plastic surgery, ',
              'MS Cardiothoracic surgery, ', 'MS Urology, ', 'MS Cardiac surgery, ', 'MS Cosmetic surgery, ',
              'MS ENT, ',
              'MS Ophthalmology, ', 'MS Gynecology, ', 'MS Obstetrics, ', 'MS Orthopedics, ']
    str = 'MBBS, '
    index = random.randint(0, 22)
    str = str + edlist[index]
    return str


# GENERATING MRN - UNIQUE ID
def getuniqId():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return x


# GENERATE FAKE ADDRESS
def getAddr():
    fake = Faker()
    addr = fake.address()
    return addr


# GENERATE DATE OF BIRTH - RANDOM
def getDOB():
    start_date = datetime.date(1955, 1, 1)
    end_date = datetime.date(1990, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return str(random_date)


# RANDOM PINCODE GENERATOR
def getPincode():
    digits = "0123456789"
    pin = ""
    for i in range(6):
        pin += digits[math.floor(random.random() * 10)]
    return pin


def getState():
    str = ""
    statelist = ['Andhra Pradesh', 'Assam', 'Arunachal Pradesh', 'Bihar', 'Goa', 'Gujarat', 'Jammu and Kashmir',
                 'Jharkhand', 'West Bengal', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
                 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura',
                 'Uttaranchal', 'Uttar Pradesh', 'Haryana', 'Himachal Pradesh', 'Chhattisgarh']
    index = random.randint(0, 27)
    str = str + statelist[index]
    return str


# MAIN
data = []
for i in range(50000):
    uniqId = getuniqId()
    name = getName().split(" ")
    fName = name[0]
    lName = name[1]
    primary_phone = random_phone_num_generator()
    sec_phone = random_phone_num_generator()
    exp = assignYOE()
    # Assigning no. of specialiasion by assigning a random value within (1,2)
    no_of_spez = randint(1, 2)
    spez = getSpecialization(no_of_spez)
    edu = getEducation()
    dob = getDOB()
    email = fName + "." + lName + "@email.com"
    pincode = getPincode()
    state = getState()
    data.append([uniqId, fName, lName, dob, primary_phone, sec_phone, email, pincode, state, exp, spez, edu])

dataFrame = pd.DataFrame(data, columns=['MRN Number', 'First Name', 'Last Name', 'DOB', 'Primary Phone Number',
                                        'Secondary Phone Number', 'Email', 'Pincode', 'State', 'Years of Exp.',
                                        'Specialization', 'Education'])
dataFrame.to_csv('Generated.csv')
print('DataGenerated - check CSV file in directory')
