import random
import time

from Pages.AlertsFrameWindowsPage import BrowserWindow, AlertWindow, Frames, NestedFrames, ModalDialogs
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

class TestFrames:

    def testFirstFrame(self, driver):
        page = Frames(driver, "https://demoqa.com/frames")
        page.openUrl()
        result = page.ReturnFirstFrameTextAndSize()
        assert result == ['This is a sample page', '500px', '350px']

    def testSecondFrame(self, driver):
        page = Frames(driver, "https://demoqa.com/frames")
        page.openUrl()
        result = page.ReturnSecondFrameTextAndSize()
        assert result == ['This is a sample page', '100px', '100px']

class TestNestedFrame:

    def testNestedFrame(self, driver):
        page = NestedFrames(driver, "https://demoqa.com/nestedframes")
        page.openUrl()
        parentText, childText = page.GetTextFromNestedFrames()
        assert parentText == "Parent frame" and childText == "Child Iframe", "Text in frame is different"

class TestModalDialogs:

    def testFirstFrame(self, driver):
        page = ModalDialogs(driver, "https://demoqa.com/modal-dialogs")
        page.openUrl()
