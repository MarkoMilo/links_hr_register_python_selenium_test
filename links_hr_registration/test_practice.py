import pytest
import random
import time
from common import zip_codes_croatia
from common import choose_zipcode
from common import months

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


PATH = Service("C:/Program Files (x86)/chromedriver.exe")  # podesi putanju ka Chrome web drajveru
driver = webdriver.Chrome(service=PATH)

WEBSIT_URL = "https://www.links.hr/hr/register"

x = ["passwordww", "password1ww"]


@pytest.mark.parametrize("password1, confirmation_password", [(x[0], x[1])])
def test_password_confirmation(password1, confirmation_password):
    driver.get(WEBSIT_URL)  # Open website
    driver.implicitly_wait(4)
    print("\n**************\npassword1: ", password1)
    print("\n**************\nconfirmation_password: ", confirmation_password)