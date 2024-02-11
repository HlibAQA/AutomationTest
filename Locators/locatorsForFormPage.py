import random

from selenium.webdriver.common.by import By

from Locators.locatorForElementPage import LocatorsForWebTables


class LocatorsFormPage:

    first_name_input = LocatorsForWebTables.first_name_input
    last_name_input = LocatorsForWebTables.last_name_input
    email_input = LocatorsForWebTables.email_input
    gender_radio_button = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    hobbies_radio_button = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1,3)}']")
    mobile_number_input = (By.CSS_SELECTOR, "input[id='userNumber']")
    subjects_input = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    upload_picture_button = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    current_address_input = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    state_input = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    city_input = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    submit_button = (By.CSS_SELECTOR, "button[id='submit']")
    subjects_data = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Economics", "Economics", "Arts", "Social Studies", "History", "Civics"]
    listWithStateAndCity = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }
    date_of_birth = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")