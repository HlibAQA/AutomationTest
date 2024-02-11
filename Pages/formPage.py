import os
import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Locators.locatorsFormPage import LocatorsFormPage
from Pages.basePage import BasePage
from generator.generator import generatedNames, generatedFile
from Pages.elementPage import WebTablesPage


class FormPage(BasePage):
    locators = LocatorsFormPage()

    def AddNewUser(self):

        state = random.choice(list(self.locators.listWithStateAndCity.keys()))
        city = random.choice(self.locators.listWithStateAndCity.get(state))
        gender = self.elementIsVisible(self.locators.gender_radio_button)
        hobbie = self.elementIsVisible(self.locators.hobbies_radio_button)
        subject = random.choice(self.locators.subjects_data)
        self.removeAdWithFooter()
        maxMobileNumberLen = int(self.elementIsVisible(self.locators.mobile_number_input).get_attribute('maxlength'))
        credential = next(generatedNames(maxMobileNumberLen))
        fileName, path = generatedFile()

        #starting test
        self.elementIsVisible(self.locators.first_name_input).send_keys(credential.fullName)
        self.elementIsVisible(self.locators.last_name_input).send_keys(credential.lastName)
        self.elementIsVisible(self.locators.email_input).send_keys(credential.email)
        genderText = gender.text
        gender.click()
        self.elementIsVisible(self.locators.mobile_number_input).send_keys(credential.mobileNumber)
        dateOfBirth = self.elementIsVisible(self.locators.date_of_birth).get_attribute('value')
        self.elementIsVisible(self.locators.date_of_birth).click()
        monthOfBirth = self.driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__current-month")]').text
        self.elementIsVisible(self.locators.mobile_number_input).click()
        self.elementIsVisible(self.locators.subjects_input).send_keys(subject)
        self.elementIsVisible(self.locators.subjects_input).send_keys(Keys.RETURN)
        hobbiesText = hobbie.text
        hobbie.click()
        self.elementIsVisible(self.locators.upload_picture_button).send_keys(path)
        os.remove(path)
        self.elementIsVisible(self.locators.current_address_input).send_keys(credential.currentAddress)
        self.elementIsVisible(self.locators.state_input).send_keys(state)
        self.elementIsVisible(self.locators.state_input).send_keys(Keys.RETURN)
        self.elementIsVisible(self.locators.city_input).send_keys(city)
        self.elementIsVisible(self.locators.city_input).send_keys(Keys.RETURN)
        self.elementIsVisible(self.locators.submit_button).click()
        return ([credential.fullName + " " + credential.lastName, credential.email, genderText, str(credential.mobileNumber), dateOfBirth[:2] + " " +
                 monthOfBirth.replace(" ", ","), subject, hobbiesText, fileName, str(credential.currentAddress).replace('\n', ' '), state + " " + city])

    def GetResultFromFormPage(self):
            result = self.driver.find_elements(By.XPATH, "//div[@class='table-responsive']//td[2]")
            data = []
            for item in result:
                data.append(item.text)
            return data

    def CheckValidationForFields(self):
        self.removeAdWithFooter()
        self.elementIsVisible(self.locators.submit_button).click()
        time.sleep(1)
        firstNameIsValid = self.IsFieldValidated(self.elementIsVisible(self.locators.first_name_input))
        secondNameIsValid = self.IsFieldValidated(self.elementIsVisible(self.locators.last_name_input))
        mobileNumberIsValid = self.IsFieldValidated(self.elementIsVisible(self.locators.mobile_number_input))
        genderButtonIsValid = self.IsRadioButtonValidated(self.elementIsVisible(self.locators.gender_radio_button))
        return firstNameIsValid, secondNameIsValid, mobileNumberIsValid, genderButtonIsValid