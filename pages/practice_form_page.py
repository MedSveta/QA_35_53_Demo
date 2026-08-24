from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from models.student import Student


class PracticeFormPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput' "
                               "or @class='form-control react-datepicker-ignore-onclickoutside']")
    SUBJECTS = (By.CSS_SELECTOR, "input#subjectsInput.subjects-auto-complete__input")
    CURR_ADDRESS = (By.XPATH, "//textarea[@placeholder='Current Address']")
    STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    BTN_SUBMIT = (By.XPATH, "//button[text()='Submit']")

    def fill_and_click_submit(self, student: Student) -> None:
        self.fill(self.FIRST_NAME, student.first_name)
        self.fill(self.LAST_NAME, student.last_name)
        self.fill(self.EMAIL, student.email)
