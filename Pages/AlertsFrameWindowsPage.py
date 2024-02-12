import time

from Locators.locatorsAlertsFrameWindowsPage import LocatorsBrowserWindow, LocatorsAlert, LocatorsFrames, \
    LocatorsNestedFrames, LocatorsModalDialog
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

class Frames(BasePage):

    locators = LocatorsFrames()

    def ReturnFirstFrameTextAndSize(self):
        return self.GetFrameTextAndSize(self.locators.first_frame, self.locators.frame_text)

    def ReturnSecondFrameTextAndSize(self):
        return self.GetFrameTextAndSize(self.locators.second_frame, self.locators.frame_text)

class NestedFrames(BasePage):

    locators = LocatorsNestedFrames()

    def GetTextFromNestedFrames(self):
        parentFrame = self.elementIsPresented(self.locators.parent_frame)
        self.driver.switch_to.frame(parentFrame)
        parentText = self.elementIsPresented(self.locators.parent_text).text

        childFrame = self.elementIsPresented(self.locators.child_frame)
        self.driver.switch_to.frame(childFrame)
        childText = self.elementIsPresented(self.locators.child_text).text

        self.driver.switch_to.default_content()
        return parentText, childText

class ModalDialogs(BasePage):

    locators = LocatorsModalDialog()