import numpy as np
import pandas as pd
import random
import names
import string
from faker import Faker


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
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return x


# GENERATE FAKE ADDRESS
def getAddr():
    fake = Faker()
    addr = fake.address()
    return addr


# MAIN
data = []
for i in range(50000):
    uniqId = getuniqId()
    name = getName().split(" ")
    fName = name[0]
    lName = name[1]
    phone = random_phone_num_generator()
    exp = assignYOE()
    # Assigning no. of specialiasion by assigning a random value within (1,2,3)
    no_of_spez = random.randint(1, 2)
    spez = getSpecialization(no_of_spez)
    edu = getEducation()
    addr = getAddr()
    data.append([uniqId, fName, lName, phone, exp, spez, edu,addr])

dataFrame = pd.DataFrame(data, columns=['MRN Number', 'First Name', 'Last Name', 'Phone Number', 'Years of Exp.',
                                        'Specialization', 'Education', 'Address'])
dataFrame.to_csv('Generated.csv')
print('DataGenerated - check CSV file in directory')
