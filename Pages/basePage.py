from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as excon


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def openUrl(self):
        self.driver.get(self.url, )

    def elementIsVisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(excon.visibility_of_element_located(locator))

    def elementsAreAllVisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(excon.visibility_of_all_elements_located(locator))

    def elementIsPresented(self, locator, timeout=5):
        return wait(self.driver, timeout).until(excon.presence_of_element_located(locator))

    def elementsAreAllNotVisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(excon.presence_of_all_elements_located(locator))

    def elementIsInvisible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(excon.invisibility_of_element_located(locator))

    def elementIsClicable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(excon.element_to_be_clickable(locator))

    def scrollToElement(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def doubleClick(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def rightClick(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def removeAdWithFooter(self):
        self.driver.execute_script("document.getElementById('fixedban').remove();")
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    def IsFieldValidated(self, locator):
        fieldColor = locator.value_of_css_property("border-color")
        #rgb(220, 53, 69) is correct color
        if str(fieldColor) == "rgb(220, 53, 69)":
            return True
        else:
            return False

    def IsRadioButtonValidated(self, locator):
        radioButtonColor = locator.value_of_css_property("color")
        # rgb(220, 53, 69) is correct color
        if str(radioButtonColor) == "rgba(220, 53, 69, 1)":
            return True
        else:
            return False

    def ReturnUrlForNewWindowTab(self, locator):
        locator.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return self.driver.current_url
