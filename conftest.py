import os
import pytest
from selenium import webdriver
from selenium.webdriver.remote import remote_connection
from pageobject.methods import *
import time


@pytest.fixture(scope='class')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('/Users/sah_m/Desktop/Foravtotests/chromedriver 4')
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope='class')
def avtorithaision(browser, login='141', password='19468персик'):
    browser.get('https://57211.shot-uchi.ru/')
    login_input = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(login_1)
    time.sleep(3)
    password_input = wdw(browser, 35).until(EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_1)
    enter = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()

