"""
This is file just for testing python features, a small piece of code.
IGNORE this file
"""
from selenium.common.exceptions import NoSuchElementException, TimeoutException

"""
RUN TESTS FROM TERMINAL:
pytest -v -s --html=.\\reports\registration_page.html --self-contained-html test_registration_page.py
"""

import random
import time
from common import zip_codes_croatia
from common import choose_zipcode
from common import months
from common import random_string
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


WEBSITE_URL = "https://www.links.hr/hr/register"

PATH = Service("C:/Program Files (x86)/chromedriver.exe")  # podesi putanju ka Chrome web drajveru
driver = webdriver.Chrome(service=PATH)
driver.get(WEBSITE_URL)  # Open website using webdriver
driver.implicitly_wait(10)

# buttons = driver.find_elements(By.CSS_SELECTOR, "body.color-neutral.notAndroid23:nth-child(2) "
#                                                                  "div.master-wrapper-page:nth-child(12) "
#                                                                  "div.master-wrapper-content "
#                                                                  "div.master-wrapper-main:nth-child(8) div.center-1 "
#                                                                  "div.page.registration-result-page:nth-child(1) "
#                                                                  "div.page-body div.buttons > "
#                                                                  "input.button-1.register-continue-button")

try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body.color-neutral.notAndroid23:nth-child(2) "
                                                                 "div.master-wrapper-page:nth-child(12) "
                                                                 "div.master-wrapper-content "
                                                                 "div.master-wrapper-main:nth-child(8) div.center-1 "
                                                                 "div.page.registration-result-page:nth-child(1) "
                                                                 "div.page-body div.buttons > "
                                                                 "input.button-1.register-continue-button")))
except TimeoutException:
    assert "Element doesn't exist"



try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body.color-neutral.notAndroid23:nth"
                                                                                 "-child(2) "
                                                                                 "div.master-wrapper-page:nth-child("
                                                                                 "12) div.header-menu:nth-child(8) "
                                                                                 "ul.mega-menu:nth-child(3) "
                                                                                 "li.mega-menu-responsive-root-hide:nth-child(1) > a.submenuLink.akcije")))
except TimeoutException:
    assert not "Element doesn't exist"

# print(driver.find_element(By.CSS_SELECTOR, "body.color-neutral.notAndroid23:nth-child(2) "
#                                                                  "div.master-wrapper-page:nth-child(12) "
#                                                                  "div.master-wrapper-content "
#                                                                  "div.master-wrapper-main:nth-child(8) div.center-1 "
#                                                                  "div.page.registration-result-page:nth-child(1) "
#                                                                  "div.page-body div.buttons > "
#                                                                  "input.button-1.register-continue-button"))


