import time

from Locators.locatorsAlertsFrameWindowsPage import LocatorsBrowserWindow
from Pages.basePage import BasePage
from selenium import webdriver


class BrowserWindow(BasePage):
    locators = LocatorsBrowserWindow()

    def OpenNewTab(self):
        return self.ReturnUrlForNewWindowTab(self.elementIsVisible(self.locators.new_tab_button))

    def OpenNewWindow(self):
        return self.ReturnUrlForNewWindowTab(self.elementIsVisible(self.locators.new_window_button))

