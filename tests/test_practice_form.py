from pages.home_page import HomePage

class TestFormPage:
    def test_open_practice_form(self, driver):
        forms_page = HomePage(driver).open().open_forms()