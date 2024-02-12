import time

from Locators.locatorsAlertsFrameWindowsPage import LocatorsBrowserWindow, LocatorsAlert
from Pages.basePage import BasePage
from selenium import webdriver


class BrowserWindow(BasePage):
    locators = LocatorsBrowserWindow()

    def OpenNewTab(self):
        return self.ReturnUrlForNewWindowTab(self.elementIsVisible(self.locators.new_tab_button))

    def OpenNewWindow(self):
        return self.ReturnUrlForNewWindowTab(self.elementIsVisible(self.locators.new_window_button))

class AlertWindow(BasePage):
    locators = LocatorsAlert()

    def GetTextFromAlert(self):
        self.elementIsVisible(self.locators.alert_button).click()
        alert = self.driver.switch_to.alert
        return alert.text

    def GetTextFromPositiveConfirmationAlert(self):
        self.elementIsVisible(self.locators.alert_confirmation_button).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        return self.elementIsPresented(self.locators.confirm_text).text

    def GetTextFromNegativeConfirmationAlert(self):
        self.elementIsVisible(self.locators.alert_confirmation_button).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        return self.elementIsPresented(self.locators.confirm_text).text

    def GetTextFromPromptAlert(self, text):
        self.elementIsVisible(self.locators.prompt_button).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        return self.elementIsPresented(self.locators.prompt_text).text