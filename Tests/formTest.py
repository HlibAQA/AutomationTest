import time

from Pages.formPage import FormPage
from conftest import driver


class TestFormPage:
    def testAddUserForFormPage(self, driver):
        page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        page.openUrl()
        resultInput = page.AddNewUser()
        resultOutput = page.GetResultFromFormPage()
        assert resultInput == resultOutput

    def testValidationForFieldsFormPage(self, driver):
        page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        page.openUrl()
        result = page.CheckValidationForFields()
        assert True in result