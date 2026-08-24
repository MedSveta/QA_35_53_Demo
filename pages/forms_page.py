from selenium.webdriver.common.by import By
from pages.practice_form_page import PracticeFormPage

from pages.base_page import BasePage

class FormsPage(BasePage):
   PRACTICE_FORM_LINK = (By.XPATH, "//span[text()='Practice Form']")

   def open_practice_form(self) -> PracticeFormPage:
       self.click(self.PRACTICE_FORM_LINK)
       return PracticeFormPage(self.driver)