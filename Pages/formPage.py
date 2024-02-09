import os
import random
import time

from selenium.webdriver import Keys

from Locators.locatorsForFormPage import LocatorsFormPage
from Pages.basePage import BasePage
from generator.generator import generatedNames, generatedFile


class FormPage(BasePage):
    locators = LocatorsFormPage()

    def AddNewUser(self):

        state = random.choice(list(self.locators.listWithStateAndCity.keys()))
        city = random.choice(self.locators.listWithStateAndCity.get(state))
        subject = random.choice(self.locators.subjects_data)
        self.removeAdWithFooter()
        maxMobileNumberLen = int(self.elementIsVisible(self.locators.mobile_number_input).get_attribute('maxlength'))
        credential = next(generatedNames(maxMobileNumberLen))
        fileName, path = generatedFile()
        self.elementIsVisible(self.locators.first_name_input).send_keys(credential.fullName)
        self.elementIsVisible(self.locators.last_name_input).send_keys(credential.lastName)
        self.elementIsVisible(self.locators.email_input).send_keys(credential.email)
        self.elementIsPresented(self.locators.gender_radio_button).click()
        self.elementIsVisible(self.locators.mobile_number_input).send_keys(credential.mobileNumber)
        self.elementIsVisible(self.locators.subjects_input).send_keys(subject)
        self.elementIsVisible(self.locators.subjects_input).send_keys(Keys.RETURN)
        self.elementIsPresented(self.locators.hobbies_radio_button).click()
        self.elementIsVisible(self.locators.upload_picture_button).send_keys(path)
        os.remove(path)
        self.elementIsVisible(self.locators.current_address_input).send_keys(credential.currentAddress)
        self.elementIsVisible(self.locators.state_input).send_keys(state)
        self.elementIsVisible(self.locators.state_input).send_keys(Keys.RETURN)
        self.elementIsVisible(self.locators.city_input).send_keys(city)
        self.elementIsVisible(self.locators.city_input).send_keys(Keys.RETURN)
        self.elementIsVisible(self.locators.submit_button).click()
        return ([credential.fullName + " " + credential.lastName, credential.email, credential.mobileNumber, subject,
              fileName, str(credential.currentAddress).replace('\n', ' '), state + " " + city])