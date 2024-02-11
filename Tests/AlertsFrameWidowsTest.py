import time

from Pages.AlertsFrameWindowsPage import BrowserWindow
from conftest import driver


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
