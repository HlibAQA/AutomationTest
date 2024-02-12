import random
import time

from Pages.AlertsFrameWindowsPage import BrowserWindow, AlertWindow
from conftest import driver
from generator.generator import generatedNames


class TestBrowserWindows:

    def testOpenNewTab(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.openUrl()
        result = page.OpenNewTab()
        assert result == "https://demoqa.com/sample", "The opened URL for tab is incorrect"

    def testOpenNewWindow(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.openUrl()
        result = page.OpenNewWindow()
        assert result == "https://demoqa.com/sample", "The opened URL for window is incorrect"


class TestAlerts:

    def testUsualAlert(self, driver):
        page = AlertWindow(driver, "https://demoqa.com/alerts")
        page.openUrl()
        result = page.GetTextFromAlert()
        assert result == "You clicked a button", "The Alerts is not displayed"

    def testPositiveConfirmationAlert(self, driver):
        page = AlertWindow(driver, "https://demoqa.com/alerts")
        page.openUrl()
        result = page.GetTextFromPositiveConfirmationAlert()
        assert result == "You selected Ok", "The chosen button is Cancel"

    def testNegativeConfirmationAlert(self, driver):
        page = AlertWindow(driver, "https://demoqa.com/alerts")
        page.openUrl()
        result = page.GetTextFromNegativeConfirmationAlert()
        assert result == "You selected Cancel", "The chosen button is Ok"

    def testPromptAlert(self, driver):
        page = AlertWindow(driver, "https://demoqa.com/alerts")
        page.openUrl()
        text = next(generatedNames())
        result = page.GetTextFromPromptAlert(text.fullName)
        assert result == f"You entered {text.fullName}", "Name is not matched with result"
