import time

from Pages.formPage import FormPage
from conftest import driver


class TestFormPage:
    def testAddUserForFormPage(self, driver):
        page = FormPage(driver, "https://demoqa.com/automation-practice-form")
        page.openUrl()
        resultInput = page.AddNewUser()
        time.sleep(1)
        resultOutput = page.GetREsultFromFormPage()
        assert resultInput == resultOutput