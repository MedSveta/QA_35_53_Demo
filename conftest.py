import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker

from models.student import Student
from models.enums import Gender, Hobbies, StateCity

fake = Faker()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(2)
    driver.quit()


@pytest.fixture
def student() -> Student:
    return Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        gender=Gender.FEMALE,
        mobile=fake.numerify("##########"),
        date_of_birth="22 Nov 1999",
        subject="Math,English,History",
        hobbies=[Hobbies.SPORTS, Hobbies.READING, Hobbies.MUSIC],
        picture="",
        curr_address="Street 1 app. 67",
        state=StateCity.RAJASTHAN.state,
        city=StateCity.RAJASTHAN.cities[0],
    )
