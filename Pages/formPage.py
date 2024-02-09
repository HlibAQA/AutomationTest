from Locators.locatorsForFormPage import LocatorsFormPage
from Pages.basePage import BasePage


class FormPage(BasePage):
    locators = LocatorsFormPage()

    def AddNewUser(self):
        pass