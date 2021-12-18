import random
import time
from common import zip_codes_croatia
from common import choose_zipcode
from common import months
from common import random_string
import pytest
from pytest_html_reporter import attach

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

PATH = Service("C:/Program Files (x86)/chromedriver.exe")  # podesi putanju ka Chrome web drajveru
driver = webdriver.Chrome(service=PATH)

WEBSITE_URL = "https://www.links.hr/hr/register"
GENDER = ["gender-male", "gender-female"]

tc1 = ["username", "pass1234"]


def test_setup():
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.implicitly_wait(5)
    # driver.close()


def test_open_page():
    driver.get(WEBSITE_URL)  # Open website
    driver.implicitly_wait(10)
    site_title = driver.title
    assert site_title == "Registrirajte se - Links"


def get_var_name(var):
    vnames = [name for name in globals() if globals()[name] is var]
    return vnames[-1]


tc_10_1 = ["password", "password1", "tc_10_1"]


@pytest.mark.parametrize("password1, confirmation_password, text1", [(tc_10_1[0], tc_10_1[1], tc_10_1[2])])
def test_password_confirmation(password1, confirmation_password, text1):
    driver.get(WEBSITE_URL)  # Open website
    driver.implicitly_wait(5)
    password = driver.find_element(By.ID, "Password")
    password.send_keys(password1)

    confirm_password = driver.find_element(By.ID, "ConfirmPassword")
    confirm_password.send_keys(confirmation_password)

    tmp = driver.find_element(By.CLASS_NAME, "field-validation-error")
    print(tmp.text)
    attach(data=driver.get_screenshot_as_png())
    assert tmp.text, f"\n\nTest Case: {text1}.\nPassword: {password1}\nPassword: {confirmation_password}\nActual status {tmp.text}.\n"


tc_9_1 = ["password", "password1", "tc_9_1"]


@pytest.mark.parametrize("pswd, conf_pswd, text1", [(tc_9_1[0], tc_9_1[1], tc_9_1[2])])
def test_is_password_hidden(pswd, conf_pswd, text1):
    driver.get(WEBSITE_URL)  # Open website
    driver.implicitly_wait(1)
    password = driver.find_element(By.ID, "Password")
    password.send_keys(pswd)
    p = password.is_displayed()
    confirm_password = driver.find_element(By.ID, "ConfirmPassword")
    confirm_password.send_keys(conf_pswd)
    attach(data=driver.get_screenshot_as_png())
    assert p
    assert confirm_password.is_displayed()
    # driver.quit()


def test_tc_7_1():
    driver.get(WEBSITE_URL)  # Open website
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, By.ID, "register-button")))
        not_found = False
    except:
        not_found = True
    assert not_found, f"\n\nTest Case: tc_7_1.\n"
    # driver.quit()


tc_12_1 = ["email", "email@", "@email.com", random_string()]


@pytest.mark.parametrize("email", [i for i in tc_12_1])
def test_tc_12_1(email):
    driver.get(WEBSITE_URL)
    driver.implicitly_wait(1)
    wrong_email_format = driver.find_element(By.ID, "Email")
    wrong_email_format.send_keys(email, Keys.TAB)

    tmp = driver.find_element(By.CLASS_NAME, "field-validation-error")
    time.sleep(3)
    wrong_email_format.clear()
    assert tmp.text
    # assert not_found, f"\n\nTest Case: tc_7_1.\n"


tc_13_1 = []


def test_tc_13_1():
    driver.get(WEBSITE_URL)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, random.choice(GENDER)))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "FirstName"))).send_keys("Marko")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "LastName"))).send_keys("Milosavljevic")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthDay"))).send_keys(random.randint(1, 12))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthMonth"))).send_keys(
        random.choice(months))  # choice random months
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthYear"))).send_keys(
        random.randint(1911, 2021))  # choice random year between 1911-2021
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Email"))).send_keys("marko87milosavljevic+test10@gmail.com")
    street_address = driver.find_element(By.ID, "StreetAddress")
    street_address.send_keys("Majevicka 10")
    street_address.send_keys(Keys.TAB, choose_zipcode()[1], Keys.ARROW_DOWN)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Phone"))).send_keys("+381695361274")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "Newsletter"))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Password"))).send_keys("password")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ConfirmPassword"))).send_keys("password")

    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button-1 register-next-step-button"))).click()

    # driver.find_element(By.ID, random.choice(GENDER)).click()
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "FirstName").send_keys("Marko")
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "LastName").send_keys("Milosavljevic")
    # driver.implicitly_wait(4)
    # driver.find_element(By.NAME, "DateOfBirthDay").send_keys(random.randint(1, 12))
    # driver.implicitly_wait(4)
    # driver.find_element(By.NAME, "DateOfBirthMonth").send_keys(random.choice(months))  # choice random months
    # driver.implicitly_wait(4)
    # driver.find_element(By.NAME, "DateOfBirthYear").send_keys(random.randint(1911, 2021))  # choice random year between 1911-2021
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "Email").send_keys("marko87milosavljevic+test10@gmail.com")
    # driver.implicitly_wait(4)
    # street_address = driver.find_element(By.ID, "StreetAddress")
    # driver.implicitly_wait(4)
    # street_address.send_keys("Majevicka 10")
    # driver.implicitly_wait(4)
    # street_address.send_keys(Keys.TAB, choose_zipcode()[1], Keys.ARROW_DOWN)
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "Phone").send_keys("+381695361274")
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "Newsletter").click()
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "Password").send_keys("password")
    # driver.implicitly_wait(4)
    # driver.find_element(By.ID, "ConfirmPassword").send_keys("password")
    # driver.implicitly_wait(4)

    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#register-button"))).click()

    # EC.element_to_be_clickable((By.XPATH, "//input[@id='register-button']"))).click()


    # driver.find_element(By.ID, "register-button").click()
    # driver.implicitly_wait(4)
    # sub = driver.find_element(By.ID, "result")
    # driver.implicitly_wait(4)
    # print(sub.text)

"""tc_15_1 = []


def test_tc_15_1():
    driver.get(WEBSITE_URL)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, random.choice(GENDER)))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "FirstName"))).send_keys("Marko")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "LastName"))).send_keys("Milosavljevic")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthDay"))).send_keys(random.randint(1, 12))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthMonth"))).send_keys(
        random.choice(months))  # choice random months
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthYear"))).send_keys(
        random.randint(1911, 2021))  # choice random year between 1911-2021
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Email"))).send_keys("marko87milosavljevic+test10@gmail.com")
    street_address = driver.find_element(By.ID, "StreetAddress")
    street_address.send_keys("Majevicka 10")
    street_address.send_keys(Keys.TAB, choose_zipcode()[1], Keys.ARROW_DOWN)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Phone"))).send_keys("+381695361274")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "Newsletter"))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Password"))).send_keys("password")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "ConfirmPassword"))).send_keys("password")

    WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button-1 register-next-step-button"))).click()"""
# tc_11_1 = []
# def test_tc_11_1():
#     birthday = driver.find_element(By.NAME, "DateOfBirthDay")
#     birthday.send_keys(12)
#
#     birthmonth = driver.find_element(By.NAME, "DateOfBirthMonth")
#     birthmonth.send_keys("prosinac")  # choice random months
#
#     birthyear = driver.find_element(By.NAME, "DateOfBirthYear")
#     birthyear.send_keys(2021)  # choice random yesr between 1911-2021


# def test_scenario():
#     rod = driver.find_element(By.ID, "gender-male")
#     rod.click()
#     first_name = driver.find_element(By.ID, "FirstName")
#     first_name.send_keys("Marko")
#     last_name = driver.find_element(By.ID, "LastName")
#     last_name.send_keys("Milosavljevic")
#
#     DateOfBirthDay = driver.find_element(By.NAME, "DateOfBirthDay")
#     DateOfBirthDay.send_keys(random.randint(1, 12))
#
#     DateOfBirthMonth = driver.find_element(By.NAME, "DateOfBirthMonth")
#     DateOfBirthMonth.send_keys(random.choice(months))  # choice random months
#
#     DateOfBirthYear = driver.find_element(By.NAME, "DateOfBirthYear")
#     DateOfBirthYear.send_keys(random.randint(1911, 2021))  # choice random yesr between 1911-2021
#
#     Email = driver.find_element(By.ID, "Email")
#     Email.send_keys("marko87milosavljevic")
#
#     street_address = driver.find_element(By.ID, "StreetAddress")
#     street_address.send_keys("Majevicka 10")
#     street_address.send_keys(Keys.TAB, "21232", Keys.ARROW_DOWN)
#
#     Phone = driver.find_element(By.ID, "Phone")
#     Phone.send_keys("+381695361274")
#
#     newsletter = driver.find_element(By.ID, "Newsletter")
#     newsletter.click()
#
#     Password = driver.find_element(By.ID, "Password")
#     Password.send_keys("password")
#
#     confirm_password = driver.find_element(By.ID, "ConfirmPassword")
#     confirm_password.send_keys("password")
