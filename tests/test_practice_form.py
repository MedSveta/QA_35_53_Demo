import time
import pytest_check as check

from pages.home_page import HomePage
from selenium.webdriver.common.by import By

FIRST_NAME = (By.XPATH, "//tbody/tr[1]/td[2]")
TEXT_FORM = "Thanks for submitting the form"


class TestFormPage:
    def test_open_practice_form(self, driver, student):
        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(5)
        practice_forms_page.fill_and_click_submit(student)

        #assert practice_forms_page.check_message() == "Thanks fo submitting the form"
        print("Test working")
        assert practice_forms_page.check_message() == TEXT_FORM

    def test_submit_check_data_in_table(self, driver, student):
        practice_forms_page = HomePage(driver).open().open_forms().open_practice_form()
        time.sleep(5)
        practice_forms_page.fill_and_click_submit(student)

        check.equal(practice_forms_page.check_message(), TEXT_FORM)
        check.is_in(student.first_name, driver.find_element(*FIRST_NAME).text)
        check.equal(practice_forms_page.check_message(), "TEXT_FORM")
        print("Test working")
        check.is_in(student.last_name, driver.find_element(*FIRST_NAME).text)


