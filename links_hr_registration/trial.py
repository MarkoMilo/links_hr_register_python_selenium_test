"""
This is file just for testing python features, a small piece of code.
IGNORE this file
"""
from selenium.common.exceptions import NoSuchElementException

"""
RUN TESTS FROM TERMINAL:
pytest -v -s --html=.\\reports\registration_page.html --self-contained-html test_registration_page.py
"""

import random
import time
from common import zip_codes_croatia
from common import choose_zipcode
from common import months
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


# try:
#     element=driver.find_element(By.CLASS_NAME, "text-box single-line valid")
# except NoSuchElementException:
#     print("No element found")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#newsletter-subscribe-button")))
    not_found = False
    print(not_found)
except:
    not_found = True
    print(not_found)




# assert not_found
# myElementList = driver.find_element((By.XPATH, "//input[@id='newsletter-subscribe-button']"))
# if (myElementList.is_displayed()):
#     print("postoji")
    # The element doesn't exist. findElements, in plural, returns a list of the matching elements, or an empty list if no one is found

"""
submit = driver.find_element(By.ID, "register-button")
submit.click()
driver.implicitly_wait(1)

username = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "customer-blocks")))
x = username.get_attribute("mandatory")
print("*******",x)
# assert username.get_attribute("field-validation-error") == "Elektronska pošta je potrebna"
"""

# password = driver.find_element(By.ID, "Password")
# password.send_keys("password")
# driver.implicitly_wait(1)
#
# confirm_password = driver.find_element(By.ID, "ConfirmPassword")
# confirm_password.send_keys("password1")
# driver.implicitly_wait(1)
#
#
# pass_confirmation_message = driver.find_element(By.TAG_NAME, "text-box single-line password input-validation-error")
# print(pass_confirmation_message)

# listItems = driver.find_elements(By.TAG_NAME, "li")
# for e in listItems:
#     isRequired = e.get_attribute("data-automation-id")
#     if isRequired!="" and "Required" in isRequired:
#         print(e.find_element_by_xpath(".//div/label").text)