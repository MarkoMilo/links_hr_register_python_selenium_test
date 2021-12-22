import time
from common import random_string
from test_cases import tc_10_1, tc_9_1, tc_12_1, tc_13_1, tc_13_2, tc_13_3, \
    tc_13_4, tc_14_1, tc_14_2, tc_14_3, tc_14_4, tc_15_1
import pytest
import pytest_repeat
from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

WEBSITE_URL = "https://www.links.hr/hr/register"

EMAIL = "marko87milosavljevic+{}@gmail.com".format(random_string(10))
SUBMIT_BUTTON_CSS_SELECTOR = "body.color-neutral.notAndroid23:nth-child(2) div.master-wrapper-page:nth-child(12) " \
                             "div.master-wrapper-content div.master-wrapper-main:nth-child(8) div.center-1 " \
                             "div.page.registration-result-page:nth-child(1) div.page-body div.buttons > " \
                             "input.button-1.register-continue-button"

PATH = Service("C:/Program Files (x86)/chromedriver.exe")  # Setup path to the chromedriver
driver = webdriver.Chrome(service=PATH)


def test_setup():
    driver.get(WEBSITE_URL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.implicitly_wait(5)


@pytest.fixture()
def test_tc_1_0():
    """
    TC_1_1 Verify that webpage exists
    :return:
    """
    driver.get(WEBSITE_URL)  # Open website
    driver.implicitly_wait(20)
    site_title = driver.title
    assert site_title == "Registrirajte se - Links"


@pytest.mark.repeat(3)
@pytest.mark.parametrize("pswd, conf_pswd, text1", [(tc_9_1[0], tc_9_1[1], tc_9_1[2])])
def test_tc_9_0(test_tc_1_0, pswd, conf_pswd, text1):
    password = driver.find_element(By.ID, "Password")
    password.send_keys(pswd)
    assert password.is_displayed()
    confirm_password = driver.find_element(By.ID, "ConfirmPassword")
    confirm_password.send_keys(conf_pswd)
    attach(data=driver.get_screenshot_as_png())
    assert confirm_password.is_displayed()


@pytest.mark.parametrize("password1, confirmation_password, text1", [(tc_10_1[0], tc_10_1[1], tc_10_1[2])])
def test_tc_10_0(test_tc_1_0, password1, confirmation_password, text1):
    password = driver.find_element(By.ID, "Password")
    password.send_keys(password1)

    confirm_password = driver.find_element(By.ID, "ConfirmPassword")
    confirm_password.send_keys(confirmation_password)

    tmp = driver.find_element(By.CLASS_NAME, "field-validation-error")
    print(tmp.text)
    assert tmp.text, f"\n\nTest Case: {text1}.\nPassword: {password1}\nPassword: {confirmation_password}" \
                     f"\nActual status {tmp.text}.\n"


def test_tc_7_0():
    driver.get(WEBSITE_URL)  # Open website
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, By.ID, "register-button")))
        not_found = False
    except:
        not_found = True
    assert not_found, f"\n\nTest Case: tc_7_1.\n"


@pytest.mark.parametrize("email", [i for i in tc_12_1])
def test_tc_12_0(test_tc_1_0, email):
    driver.implicitly_wait(1)
    wrong_email_format = driver.find_element(By.ID, "Email")
    wrong_email_format.send_keys(email, Keys.TAB)

    tmp = driver.find_element(By.CLASS_NAME, "field-validation-error")
    time.sleep(3)
    wrong_email_format.clear()
    assert tmp.text


@pytest.mark.parametrize("tc", [tc_13_1, tc_13_2, tc_13_3, tc_13_4])
def test_tc_13_0(test_tc_1_0, tc):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "FirstName"))).send_keys(tc.get("first_name"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "LastName"))).send_keys(tc.get("last_name"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Email"))).send_keys(tc.get("email"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Password"))).send_keys(tc.get("password"))
    confirm = driver.find_element(By.ID, "ConfirmPassword")
    confirm.send_keys(tc.get("confirm_password"))
    confirm.send_keys(Keys.TAB, Keys.ENTER)
    continue_registration = driver.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON_CSS_SELECTOR)
    print("\n\n++++++++++++++++++++++++++++++++++++++++++\n\n", continue_registration.text)
    assert continue_registration


@pytest.mark.parametrize("tc_14", [tc_14_1, tc_14_2, tc_14_3, tc_14_4])
def test_tc_14_0(test_tc_1_0, tc_14):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "FirstName"))).send_keys(tc_14.get("first_name"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "LastName"))).send_keys(tc_14.get("last_name"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Email"))).send_keys(tc_14.get("email"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Password"))).send_keys(tc_14.get("password"))
    confirm = driver.find_element(By.ID, "ConfirmPassword")
    confirm.send_keys(tc_14.get("confirm_password"))
    confirm.send_keys(Keys.TAB, Keys.ENTER)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body.color-neutral.notAndroid23:nth-child(2) "
                                                         "div.master-wrapper-page:nth-child(12) "
                                                         "div.master-wrapper-content "
                                                         "div.master-wrapper-main:nth-child(8) div.center-1 "
                                                         "div.page.registration-result-page:nth-child(1) "
                                                         "div.page-body div.buttons > "
                                                         "input.button-1.register-continue-button")))
    except TimeoutException:
        assert "Element doesn't exist"


@pytest.mark.parametrize("tc_15", [tc_15_1])
def test_tc_15_0(test_tc_1_0, tc_15):
    driver.implicitly_wait(10)
    driver.maximize_window()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "FirstName"))).send_keys(tc_15.get("first_name"))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, tc_15.get("gender")))).click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "LastName"))).send_keys(tc_15.get("last_name"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthDay"))).send_keys(tc_15.get("birthmonth"))
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthMonth"))).send_keys(
        tc_15.get("birthday"))  # choice random months
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "DateOfBirthYear"))).send_keys(
        tc_15.get("birtyear"))  # choice random year between 1911-2021
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Email"))).send_keys(tc_15.get("email"))
    street_address = driver.find_element(By.ID, "StreetAddress")
    street_address.send_keys(tc_15.get("adress"))
    street_address.send_keys(Keys.TAB, tc_15.get("zipcode"), Keys.ARROW_DOWN)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Phone"))).send_keys(tc_15.get("phone"))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "Newsletter"))).send_keys("\n")  #click()
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "Password"))).send_keys(tc_15.get("password"))
    confirm = driver.find_element(By.ID, "ConfirmPassword")
    confirm.send_keys(tc_15.get("confirm_password"))
    confirm.send_keys(Keys.TAB, Keys.ENTER)
    continue_registration = driver.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON_CSS_SELECTOR)
    print("\n\n++++++++++++++++++++++++++++++++++++++++++\n\n", continue_registration.text)
    assert continue_registration
    continue_registration.click()


def test_close(test_tc_1_0):
    driver.quit()