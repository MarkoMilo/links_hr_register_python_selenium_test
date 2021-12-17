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

PATH = Service("C:/Program Files (x86)/chromedriver.exe")  # podesi putanju ka Chrome web drajveru
driver = webdriver.Chrome(service=PATH)


driver.get("https://www.links.hr/hr/register")  # Otvorite website koriscenjem web drajvera
driver.implicitly_wait(10)
Password = driver.find_element(By.ID, "Password")
Password.send_keys("password")

confirm_password = driver.find_element(By.ID, "ConfirmPassword")
confirm_password.send_keys("password1")
driver.implicitly_wait(1)

pass_confirmation_text = driver.find_element(By.CLASS_NAME, "field-validation-error")
print(pass_confirmation_text.text)
print(type(pass_confirmation_text.text))