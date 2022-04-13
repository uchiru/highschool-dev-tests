import os
import pytest
from selenium import webdriver
from selenium.webdriver.remote import remote_connection
from pageobject.methods import *
from constance import *
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.remote import remote_connection


def pytest_addoption(parser):
    """Create options from console for tests env"""
    parser.addoption('--bn', action='store', default="chrome", help="Choose browser: chrome, remote_chrome or firefox")
    parser.addoption('--h', action='store', default="enable", help='Choose headless: enable or other')
    parser.addoption('--s', action='store', default="1920,1080", help='Size window: width,height')


@pytest.fixture(scope="class")
def browser(request):
    if request.config.getoption("bn") == "remote_chrome":
        capabilities = {
            "browserName": "chrome",
            "enableVNC": False,
            "enableVideo": False}
        url = os.environ['SELENOID_URL']
        conn = webdriver.remote.remote_connection.RemoteConnection(url, resolve_ip=False)
        print("\nstart browser for test..")
        browser = webdriver.Remote(command_executor=conn, desired_capabilities=capabilities)
        browser.maximize_window()
        yield browser
        # этот код выполнится после завершения теста
        print("\nquit browser..")
        browser.quit()
    elif request.config.getoption("bn") == "chrome":
        options = Options()
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        print("\nstart chrome browser for test..")
        yield browser
        browser.quit()


# @pytest.fixture(scope='class')
# def browser(request):
#     # return request.config.getoption("--language")
#     options = Options()
#     browser = webdriver.Chrome(options=options)
#     print("\nstart chrome browser for test..")
#     yield browser
#     browser.quit()


@pytest.fixture(scope='class')
def avtorithaision_b2t(browser, login_b2t='141', password_b2t='19468персик'):
    browser.get('https://57211.shot-uchi.ru/')
    login_input = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2t)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2t)
    enter = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def avtorithaision_b2c(browser, login_b2c='29', password_b2c='32407собор'):
    browser.get('https://57211.shot-uchi.ru/')
    login_input = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2c)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2c)
    enter = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def avtorithaision_techear(browser, login_teacher='teacher124@uchi.ru', password_teacher='1'):
    browser.get('https://57211.shot-uchi.ru/')
    login_input = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_teacher)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_teacher)
    enter = wdw(browser, 15).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()
