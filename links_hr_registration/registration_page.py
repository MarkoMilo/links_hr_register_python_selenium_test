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
DateOfBirthMonth.send_keys(random.choice(months))  # choice random months

DateOfBirthYear = driver.find_element(By.NAME, "DateOfBirthYear")
DateOfBirthYear.send_keys(random.randint(1911,2021)) # choice random yesr between 1911-2021

Email = driver.find_element(By.ID, "Email")
Email.send_keys("marko87milosavljevic")

street_address = driver.find_element(By.ID, "StreetAddress")
street_address.send_keys("Majevicka 10")
street_address.send_keys(Keys.TAB, "21232", Keys.ARROW_DOWN)

Phone = driver.find_element(By.ID, "Phone")
Phone.send_keys("+381695361274")


newsletter = driver.find_element(By.ID, "Newsletter")
newsletter.click()

Password = driver.find_element(By.ID, "Password")
Password.send_keys("password")

confirm_password = driver.find_element(By.ID, "ConfirmPassword")
confirm_password.send_keys("password")