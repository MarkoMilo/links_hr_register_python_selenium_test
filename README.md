# Webshop registration page
links_hr_register_python_selenium_test

## Prerequirements:
* Download [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/), unzip, and unziped file copy on path: *C:\Program Files (x86)*
* python 3.10
* pipenv (install: pip install pipenv)

## Instructions for running tests and generating test reports

* Download or clone project and place it on some path(hereinafter PATH)
* Open terminal/cmd/PowerShell on GIT: *PATH/links_hr_register_python_selenium_test\links_hr_registration* and run following commands:
```sh
pipenv shell
pipenv install
pytest -v --capture=tee-sys --html=.\\reports\registration_page.html --self-contained-html test_registration_page.py
```
After performing the tests, the report will be located:
*PATH\links_hrhr_register_python_selenium_test\links_hr_registration\reports\registration_page.html* 