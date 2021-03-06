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
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        capabilities = {
            "browserName": "chrome",
            "enableVNC": False,
            "enableVideo": False}
        url = os.environ['SELENOID_URL']
        conn = webdriver.remote.remote_connection.RemoteConnection(url, resolve_ip=False)
        print("\nstart browser for test..")
        browser = webdriver.Remote(command_executor=conn, desired_capabilities=capabilities, options=chrome_options)
        browser.set_window_size(1920, 1080)
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
def authorization_b2t(browser, login_b2t='141', password_b2t='19468персик'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2t)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2t)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_b2c(browser, login_b2c='29', password_b2c='32407собор'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2c)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2c)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()

@pytest.fixture(scope='class')
def authorization_b2t_6th(browser, login_b2t='17', password_b2t='5478роща'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2t)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2t)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_b2t_7th(browser, login_b2c='666', password_b2c='цветы34729'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2c)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2c)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_b2c_7th(browser, login_b2c='65', password_b2c='32950город'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2c)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2c)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_b2t_8th(browser, login_b2c='86', password_b2c='11310группа'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2c)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2c)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_b2c_8th(browser, login_b2c='42', password_b2c='кулич30491'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_b2c)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_b2c)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_techear(browser, login_teacher='min+admin@uchi.ru', password_teacher='11111111'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_teacher)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_teacher)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()


@pytest.fixture(scope='class')
def authorization_techear_7th(browser, login_teacher='teach_for_7@uchi.ru', password_teacher='11111111'):
    browser.get('https://57772.shot-uchi.ru/')
    browser.implicitly_wait(10)
    login_input = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.login_input)).send_keys(
        login_teacher)
    time.sleep(3)
    password_input = wdw(browser, 35).until(
        EC.presence_of_element_located(avtor_page_elements.password_input)).send_keys(password_teacher)
    enter = wdw(browser, 30).until(EC.presence_of_element_located(avtor_page_elements.enter_button)).click()
