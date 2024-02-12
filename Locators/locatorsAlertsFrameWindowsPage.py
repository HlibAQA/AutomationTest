from selenium.webdriver.common.by import By


class LocatorsBrowserWindow:

    new_tab_button = (By.CSS_SELECTOR, "button[id='tabButton']")
    new_window_button = (By.CSS_SELECTOR, "button[id='windowButton']")

class LocatorsAlert:

    alert_button = (By.CSS_SELECTOR, "button[id='alertButton']")
    alert_confirmation_button = (By.CSS_SELECTOR, "button[id='confirmButton']")
    confirm_text = (By.CSS_SELECTOR, "span[id='confirmResult']")
    prompt_button = (By.CSS_SELECTOR, "button[id='promtButton']")
    prompt_text = (By.CSS_SELECTOR, "span[id='promptResult']")