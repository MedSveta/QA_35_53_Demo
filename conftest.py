import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from models.student import Student


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def student() -> Student:
    return Student(
        first_name="Anna",
        last_name="Antonova",
        email="anna_antonova23@gmail.com",
        gender="female",
        mobile="0123456789",
        date_of_birth="22 Nov 1999",
        subject="Math,English,History",
        hobbies="sports",
        picture="",
        curr_address="Street 1 app. 67",
        state="NCR",
        city="Delhi",
    )