from selenium.webdriver.common.by import By

from Locators.locatorForElementPage import LocatorsForWebTables


class LocatorsFormPage:

    first_name = LocatorsForWebTables.first_name_input
    last_name = LocatorsForWebTables.last_name_input
    email = LocatorsForWebTables.email_input

    def GetGenderRadioButton(self, i):
        gender_radio_button = (By.CSS_SELECTOR, f"label[for='gender-radio-{i}']")
        return gender_radio_button
    def GetHobbieRadioButton(self, i):
        hobbie_radio_button = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{i}']")
        return hobbie_radio_button