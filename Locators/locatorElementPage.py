from selenium.webdriver.common.by import By


class Locators:

    full_name = (By.CSS_SELECTOR, "input[id='userName']")
    email = (By.CSS_SELECTOR, "input[id='userEmail']")
    current_adress = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    permanent_address = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    submit = (By.CSS_SELECTOR, "button[id='submit']")

    #result

    created_name = (By.CSS_SELECTOR, "#output #name")
    created_email = (By.CSS_SELECTOR, "#output #email")
    created_current_adress = (By.CSS_SELECTOR, "#output #currentAddress")
    created_permanent_name = (By.CSS_SELECTOR, "#output #permanentAddress")

class LocatorsForCheckBox:

    show_all_checkboxes = (By.CSS_SELECTOR, "button[title='Expand all']")
    list_with_all_check_boxes_text = (By.CSS_SELECTOR, "span[class='rct-title']")
    checked_checkbox = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    list_with_all_checked_checkbox_text = (By.XPATH, "//ancestor::span[@class='rct-title']")
    text_result = (By.CSS_SELECTOR, "span[class='text-success']")

class LocatorsForRadioButtons:

    yes_radio_button = (By.CSS_SELECTOR, "label[for='yesRadio']")
    impressive_radio_button = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    no_radio_button = (By.CSS_SELECTOR, "label[for='noRadio']")
    result_radio_button = (By.CSS_SELECTOR, "span[class='text-success']")

class LocatorsForWebTables:
    add_tables = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    first_name_input = (By.CSS_SELECTOR, "input[id='firstName']")
    last_name_input = (By.CSS_SELECTOR, "input[id='lastName']")
    email_input = (By.CSS_SELECTOR, "input[id='userEmail']")
    age_input = (By.CSS_SELECTOR, "input[id='age']")
    salary_input = (By.CSS_SELECTOR, "input[id='salary']")
    department_input = (By.CSS_SELECTOR, "input[id='department']")
    submit_button = (By.CSS_SELECTOR, "button[id='submit']")
    full_people_table = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    search_box = (By.CSS_SELECTOR, "input[id='searchBox']")
    edit_button = (By.CSS_SELECTOR, "span[id='edit-record-1']")
    delete_button = (By.CSS_SELECTOR, "span[title='Delete']")

    no_rows_text = (By.CSS_SELECTOR, "div[class='rt-noData']")

    def GetDeleteUserButtonById(self, i):
        delete_user_button = (By.CSS_SELECTOR, f"span[id='delete-record-{i}']")
        return delete_user_button

class LocatorsForButtons:

    double_click_button = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    right_click_button = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    dynamic_click_button = (By.XPATH, "//*[@class='mt-4'][2]/button")
    result_double_click = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    result_right_click = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    result_dynamic_click = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

class LocatorsForLists:

    home_link = (By.CSS_SELECTOR, "a[id='simpleLink']")

class LocatorsForDownload:

    upload_file_button = (By.CSS_SELECTOR, "input[id='uploadFile']")
    upload_file_result = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    download_file_button = (By.CSS_SELECTOR, "a[id='downloadButton']")

class LocatorsForDynamicProperties:

    color_change_button = (By.CSS_SELECTOR, "button[id='colorChange']")
    visible_after_five_sec_btn = (By.CSS_SELECTOR, "button[id='visibleAfter']")
    enable_after_five_sec_btn = (By.CSS_SELECTOR, "button[id='enableAfter']")