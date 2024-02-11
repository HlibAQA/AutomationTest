import random

from Locators.locatorsFormPage import LocatorsFormPage
from data.data import Names
from faker import Faker

faker_en = Faker()
Faker.seed()
locators = LocatorsFormPage()

def generatedNames(maxNumber = 2):
    yield Names(
        fullName=faker_en.name() + " " + faker_en.last_name(),
        firstName=faker_en.name(),
        lastName=faker_en.last_name(),
        age=random.randint(18, 90),
        salary=random.randint(1000, 10000),
        department=faker_en.job(),
        email=faker_en.email(),
        currentAddress=faker_en.address(),
        permanentAddress=faker_en.address(),
        mobileNumber=random.randint(10**(maxNumber-1), 10**maxNumber-1)
    )

def generatedFile():
    fileName = f'file#{random.randint(0, 100)}.txt'
    path = f'/Users/hlibssoev/PycharmProjects/firstTestPythonProject/{fileName}'
    with open(path, 'w+') as fullFile:
        fullFile.write(f"Hello World, I'm {random.randint(0, 100)} user")
    return fileName, path
