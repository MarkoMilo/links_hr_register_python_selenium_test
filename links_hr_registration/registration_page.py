import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


meseci = ["siječanj", "veljača", "ožujak", "travanj", "svibanj", "lipanj", "srpanj", "kolovoz", "rujan", "listopad", "studeni", "prosinac"]

PATH = Service("C:\Program Files (x86)/chromedriver.exe")  # podesi putanju ka Chrome web drajveru
driver = webdriver.Chrome(service=PATH)

driver.get("https://www.links.hr/hr/register")  # Otvorite website koriscenjem web drajvera
print(driver.title)
rod = driver.find_element(By.ID, "gender-male")
# time.sleep(5)
rod.click()
first_name = driver.find_element(By.ID, "FirstName")
first_name.send_keys("Marko")
last_name = driver.find_element(By.ID, "LastName")
last_name.send_keys("Milosavljevic")

DateOfBirthDay = driver.find_element(By.NAME, "DateOfBirthDay")
DateOfBirthDay.send_keys(random.randint(1,12))

DateOfBirthMonth = driver.find_element(By.NAME, "DateOfBirthMonth")
DateOfBirthMonth.send_keys(random.choice(meseci))  # choice random months

DateOfBirthYear = driver.find_element(By.NAME, "DateOfBirthYear")
DateOfBirthYear.send_keys(random.randint(1911,2021)) # choice random yesr between 1911-2021

street_address = driver.find_element(By.ID, "StreetAddress")
street_address.send_keys("Majevicka 10")

zip_code = driver.find_element(By.ID, "fee3dfcd-8d3a-4953-85b3-2f33a82533f9")
zip_code.send_keys(21232)

# sity = driver.find_element(By.ID, "7014f550-2f63-4b25-9f84-a34719b76535")
# sity.send_keys("Split")

