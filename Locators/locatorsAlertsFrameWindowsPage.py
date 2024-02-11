from selenium.webdriver.common.by import By


class LocatorsBrowserWindow:

    new_tab_button = (By.CSS_SELECTOR, "button[id='tabButton']")
    new_window_button = (By.CSS_SELECTOR, "button[id='windowButton']")