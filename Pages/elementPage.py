import base64
import os
import random
import time
from dataclasses import asdict
from functools import wraps
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from Locators.locatorElementPage import Locators, LocatorsForWebTables, LocatorsForButtons, LocatorsForLists, \
    LocatorsForDownload, LocatorsForDynamicProperties, LocatorsForRadioButtons, LocatorsForCheckBox
from Pages.basePage import BasePage
from generator.generator import generatedNames, generatedFile
from selenium import webdriver


class TextBoxPage(BasePage):
    locators = Locators()

    def fillAllFields(self):
        setName = next(generatedNames())
        fullName = setName.fullName
        email = setName.email
        currentAdress = str(setName.currentAddress).replace('\n', ' ')
        permanentAdress = str(setName.permanentAddress).replace('\n', ' ')
        self.elementIsVisible(self.locators.full_name).send_keys(fullName)
        self.elementIsVisible(self.locators.email).send_keys(email)
        self.elementIsVisible(self.locators.current_adress).send_keys(currentAdress)
        self.elementIsVisible(self.locators.permanent_address).send_keys(permanentAdress)
        self.elementIsVisible(self.locators.submit).click()
        return fullName, email, currentAdress, permanentAdress

    def getResult(self):
        full_name = self.elementIsPresented(self.locators.created_name).text.split(':')[1]
        emails = self.elementIsPresented(self.locators.created_email).text.split(':')[1]
        current_adress = self.elementIsPresented(self.locators.created_current_adress).text.split(':')[1]
        permanent_address = self.elementIsPresented(self.locators.created_permanent_name).text.split(':')[1]
        return full_name, emails, current_adress, permanent_address

    def GetTooltipText(self):
        self.elementIsVisible(self.locators.email).send_keys("1")
        self.elementIsVisible(self.locators.submit).click()
        emailToolTipText = self.elementIsVisible(self.locators.email).get_attribute('validationMessage')
        return emailToolTipText


class CheckBoxPage(BasePage):
    locators = LocatorsForCheckBox()

    def CheckAllThings(self):
        self.elementIsVisible(self.locators.show_all_checkboxes).click()

    def CheckList(self):
        lists = self.elementsAreAllVisible(self.locators.list_with_all_check_boxes_text)
        count = 10
        while count != 0:
            item = lists[random.randint(1, 15)]
            if count > 0:
                self.scrollToElement(item)
                item.click()
                count -= 1
            else:
                break

    def CheckCheckedCheckbox(self):
        checkBox = self.elementsAreAllNotVisible(self.locators.checked_checkbox)
        data = []
        for box in checkBox:
            item = box.find_element(By.XPATH, ".//ancestor::span[@class='rct-text']")
            data.append(item.text)
        return data

    def GetOutOutResult(self):
        texter = self.elementsAreAllNotVisible(self.locators.text_result)
        data = []
        for i in texter:
            if i.text == "wordFile":
                data.append("Word File.doc")
            elif i.text == 'excelFile':
                data.append("Excel File.doc")
            elif i.text == 'workspace':
                data.append("WorkSpace")
            else:
                data.append(i.text.capitalize())
        return data

class RadioButtonsPage(BasePage):
    locators = LocatorsForRadioButtons()

    def ClickRadioButton(self, choosen):
        choise = {'yes': self.locators.yes_radio_button,
                  'impressive': self.locators.impressive_radio_button,
                  'no': self.locators.no_radio_button}
        self.elementIsVisible(choise[choosen]).click()
        # return self.elementIsVisible(choise[choosen]).text

    def GetRadioResult(self):
        return self.elementIsVisible(self.locators.result_radio_button).text

class WebTablesPage(BasePage):
    locators = LocatorsForWebTables()

    def AddNewUser(self):
        random = next(generatedNames())
        try:
            self.elementIsVisible(self.locators.add_tables).click()
        except:
            pass
        validAmountOfSymbls = self.elementIsVisible(self.locators.department_input).get_attribute("maxlength")
        self.elementIsVisible(self.locators.first_name_input).send_keys(random.firstName)
        self.elementIsVisible(self.locators.last_name_input).send_keys(random.lastName)
        self.elementIsVisible(self.locators.email_input).send_keys(random.email)
        self.elementIsVisible(self.locators.age_input).send_keys(str(random.age))
        self.elementIsVisible(self.locators.salary_input).send_keys(str(random.salary))
        self.elementIsVisible(self.locators.department_input).send_keys(random.department[:int(validAmountOfSymbls)])
        self.elementIsVisible(self.locators.submit_button).click()
        return [random.firstName, random.lastName,
                str(random.age), random.email,
                str(random.salary), random.department[:int(validAmountOfSymbls)]]


    def CheckNumberOfUsersInTheTable(self):
        list = self.elementsAreAllVisible(self.locators.full_people_table)
        data = []
        for item in list:
            data.append(item.text.splitlines())
        return data

    def SearchUser(self, type):
        self.elementIsVisible(self.locators.search_box).send_keys(type)

    def CheckSearchResult(self):
        data = self.CheckNumberOfUsersInTheTable()
        return data[0]

    def EditUser(self):
        self.elementIsPresented(self.locators.edit_button).click()
        output = self.AddNewUser()
        self.elementIsVisible(self.locators.first_name_input).clear()
        self.elementIsVisible(self.locators.first_name_input).send_keys(output[0])
        self.elementIsVisible(self.locators.last_name_input).clear()
        self.elementIsVisible(self.locators.last_name_input).send_keys(output[1])
        self.elementIsVisible(self.locators.age_input).clear()
        self.elementIsVisible(self.locators.age_input).send_keys(output[2])
        self.elementIsVisible(self.locators.email_input).clear()
        self.elementIsVisible(self.locators.email_input).send_keys(output[3])
        self.elementIsVisible(self.locators.salary_input).clear()
        self.elementIsVisible(self.locators.salary_input).send_keys(output[4])
        self.elementIsVisible(self.locators.department_input).clear()
        self.elementIsVisible(self.locators.department_input).send_keys(output[5])
        self.elementIsVisible(self.locators.submit_button).click()
        return output

    def DeleteUser(self):
        data = self.CheckNumberOfUsersInTheTable()
        count = 0
        for item in data:
            if item == ['       ']:
                pass
            else:
                count += 1
                self.elementIsVisible(self.locators.GetDeleteUserButtonById(count)).click()
        if self.CheckNumberOfUsersInTheTable()[0] == ['       ']:
            pass
        else:
            self.DeleteUser()
        return self.elementIsVisible(self.locators.no_rows_text).text

    def CheckValidationForFields(self):
        self.elementIsVisible(self.locators.add_tables).click()
        self.elementIsVisible(self.locators.submit_button).click()
        time.sleep(1)
        isFirstNameValid = self.IsFieldValidated(self.elementIsVisible(self.locators.first_name_input))
        isLastNameValid = self.IsFieldValidated(self.elementIsVisible(self.locators.last_name_input))
        isEmailValid = self.IsFieldValidated(self.elementIsVisible(self.locators.email_input))
        isAgeValid = self.IsFieldValidated(self.elementIsVisible(self.locators.age_input))
        isSalaryValid = self.IsFieldValidated(self.elementIsVisible(self.locators.salary_input))
        isDepartmentValid = self.IsFieldValidated(self.elementIsVisible(self.locators.department_input))
        return [isFirstNameValid, isLastNameValid, isEmailValid, isAgeValid, isSalaryValid, isDepartmentValid]

class ButtonPage(BasePage):
    locators = LocatorsForButtons()

    def ClickOnTheDynamicButton(self):
        self.driver.find_element(By.XPATH, "//*[@class='mt-4'][2]/button").click()
        return self.elementIsVisible(self.locators.result_dynamic_click).text

    def DoubleClickOnTheButton(self):
        self.doubleClick(self.elementIsVisible(self.locators.double_click_button))
        return self.elementIsVisible(self.locators.result_double_click).text

    def RightClickOnTheButton(self):
        self.rightClick(self.elementIsVisible(self.locators.right_click_button))
        return self.elementIsVisible(self.locators.result_right_click).text

class LinkPage(BasePage):
    locators = LocatorsForLists()

    def ReturnStatusCodeForHomeLink(self):
        homeLink = self.elementIsVisible(self.locators.home_link)
        link_href = homeLink.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            homeLink.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            print(request.status_code)

    def ReturnStatusCodeFromLink(self, link):
        response = requests.get(link)
        return response.status_code

class DownloadAndUploadPage(BasePage):
    locators = LocatorsForDownload()

    def uploadFile(self):
        fileName, path = generatedFile()
        self.elementIsPresented(self.locators.upload_file_button).send_keys(path)
        os.remove(path)
        uploadResult = self.elementIsPresented(self.locators.upload_file_result).text
        return fileName, uploadResult.split('\\')[-1]

    def downloadFile(self):
        link = self.elementIsPresented(self.locators.download_file_button).get_attribute('href')
        link_b = base64.b64decode(link)
        pathName = '/Users/hlibssoev/PycharmProjects/firstTestPythonProject/fileName.jpg'
        with open(pathName, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(pathName)
        os.remove(pathName)
        return check_file

class DynamicPropertiesPage(BasePage):
    locators = LocatorsForDynamicProperties()

    def checkChangeColoButton(self):
        colorButton = self.elementIsPresented(self.locators.color_change_button)
        theColorBefore = colorButton.value_of_css_property('color')
        time.sleep(5)
        theColorAfter = colorButton.value_of_css_property('color')
        return theColorBefore, theColorAfter

    def checkAppearButton(self):
        try:
            self.elementIsVisible(self.locators.visible_after_five_sec_btn, 4.5).click()
        except TimeoutException:
            try:
                self.elementIsVisible(self.locators.visible_after_five_sec_btn, 5.1).click()
            except TimeoutException:
                return False
            else:
                return True

        return False

    def checkAClickableButton(self):
        try:
            self.elementIsClicable(self.locators.enable_after_five_sec_btn, 4.5).click()
        except TimeoutException:
            try:
                self.elementIsVisible(self.locators.enable_after_five_sec_btn, 5.1).click()
            except TimeoutException:
                return False
            else:
                return True

        return False
