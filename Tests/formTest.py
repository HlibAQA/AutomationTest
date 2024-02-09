from Pages.formPage import FormPage


class TestFormPage:
    def testAddUserForFormPage(self, driver):
        page = FormPage(driver, "https://demoqa.com/text-box")
        page.openUrl()