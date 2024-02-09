import random
import time

from selenium.webdriver.common.by import By

from Pages.elementPage import TextBoxPage, CheckBoxPage, qiwaPage, RadioButtonsPage, WebTablesPage, ButtonPage, LinkPage, \
    DownloadAndUploadPage, DynamicPropertiesPage
from conftest import driver


class TestTextBoxPage:
    def TestTextBox(self, driver):
        page = TextBoxPage(driver, "https://demoqa.com/text-box")
        page.openUrl()
        inPutData = page.fillAllFields()
        outPutData = page.getResult()
        assert inPutData == outPutData, "The result is not matched with the data that user types"

class TestCheckBoxPage:
     def testCheckBox(self, driver):
         page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
         page.openUrl()
         page.CheckAllThings()
         page.CheckList()
         checkBoxResult = page.CheckCheckedCheckbox()
         textResult = page.GetOutOutResult()
         assert checkBoxResult == textResult, "Checkboxes result is not matched"

class TestRadioButtonPage:
    def testRadioButtons(self, driver):
        page = RadioButtonsPage(driver, "https://demoqa.com/radio-button")
        page.openUrl()
        page.ClickRadioButton('yes')
        inputYes = page.GetRadioResult()
        page.ClickRadioButton('impressive')
        inputImpressive = page.GetRadioResult()
        page.ClickRadioButton('no')
        inputNo = page.GetRadioResult()
        assert inputYes == 'Yes', "Incorrect radio button"
        assert inputImpressive == 'Impressive'

class TestWebTablePage:
    def testNewUserWebPage(self, driver):
        page = WebTablesPage(driver, "https://demoqa.com/webtables")
        page.openUrl()
        newUser = page.AddNewUser()
        result = page.CheckNumberOfUsersInTheTable()
        assert newUser in result

    def testSearchUserWebPage(self, driver):
        page = WebTablesPage(driver, "https://demoqa.com/webtables")
        page.openUrl()
        searchUser = page.AddNewUser()[random.randint(0, 5)]
        page.SearchUser(searchUser)
        resultSearch = page.CheckSearchResult()
        assert searchUser in resultSearch

    def testEditUserWebPage(self, driver):
        page = WebTablesPage(driver, "https://demoqa.com/webtables")
        page.openUrl()
        editedUser = page.EditUser()
        page.SearchUser(editedUser[random.randint(0,5)])
        resultEdit = page.CheckSearchResult()
        assert editedUser == resultEdit

    def testDeleteUserWebPage(self, driver):
        page = WebTablesPage(driver, "https://demoqa.com/webtables")
        page.openUrl()
        result = page.DeleteUser()
        assert result == "No rows found", "Table is not empty"

    def testValidationForFields(self, driver):
        page = WebTablesPage(driver, "https://demoqa.com/webtables")
        page.openUrl()
        result = page.CheckValidationForFields()
        assert True in result

class TestClickPage:

    def testClicks(self, driver):
        page = ButtonPage(driver, "https://demoqa.com/buttons")
        page.openUrl()
        doubleClickResult = page.DoubleClickOnTheButton()
        rightClickResult = page.RightClickOnTheButton()
        dynamicClickResult = page.ClickOnTheDynamicButton()
        assert (doubleClickResult == "You have done a double click",
                rightClickResult == "You have done a right click",
                dynamicClickResult == "You have done a dynamic click"), "Something wrong"

class TestLinkPage:

    def testLink(self, driver):
        page = LinkPage(driver, "https://demoqa.com/links")
        page.openUrl()
        href, url = page.TestHomeLink()
        assert href == url, "incorrect url"

    def testBadRequestLink(self, driver):
        page = LinkPage(driver, "https://demoqa.com/links")
        page.openUrl()
        responseCode = page.TestBrokenLink()
        assert responseCode == 400, "Response is not 400"

class TestDownloadPage:

    def testUploadFile(self, driver):
        page = DownloadAndUploadPage(driver, "https://demoqa.com/upload-download")
        page.openUrl()
        fileName, result = page.uploadFile()
        assert fileName == result, "File names is not matched"

    def testDownloadFile(self, driver):
        page = DownloadAndUploadPage(driver, "https://demoqa.com/upload-download")
        page.openUrl()
        result = page.downloadFile()
        assert result is True, "File isn't downloaded"

class TestDynamicPropertiesPage:

    def testColorButton(self, driver):
        page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        page.openUrl()
        colorBefore, colorAfter = page.checkChangeColoButton()
        assert colorAfter != colorBefore, "Color is not changed"

    def testNotAppearButton(self, driver):
        page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        page.openUrl()
        result = page.checkAppearButton()
        assert result is True, "Button is appear before or after 5 sec"

    def testNotClickableButton(self, driver):
        page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        page.openUrl()
        result = page.checkAClickableButton()
        assert result is True, "Button is clickable before or after 5 sec"

class TestQiwaLoggin:
    def testQiwa(self, driver):
        page = qiwaPage(driver, "https://Qiwa:zmkqikk7XEfZ6L8Oa%2FQ%3D@auth.qiwa.tech")
        page.openUrl()
        page.LoginIntoAcc()

