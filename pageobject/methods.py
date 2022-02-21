from pageobject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from constance import *
import time
from datetime import *


def skip_over_checkbox(browser):
    math_biology_click = wdw(browser, 20).until(
        EC.presence_of_element_located(payments_page_elements.math_check_box)).click()
    rus_biology_click = wdw(browser, 20).until(
        EC.presence_of_element_located(payments_page_elements.rus_check_box)).click()
    modern_biology_click = wdw(browser, 20).until(
        EC.presence_of_element_located(payments_page_elements.eng_check_box)).click()


def new_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 30).until(EC.presence_of_element_located(headpage_elements.full_version_button)).click()
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 30).until(
            EC.presence_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 30).until(
            EC.presence_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    else:
        modern_biology_click = wdw(browser, 30).until(
            EC.presence_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 30).until(
            EC.presence_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 25).until(EC.presence_of_element_located(payments_page_elements.buy_button)).click()
    card = wdw(browser, 15).until(EC.presence_of_element_located(card_data_page_elements.card_num)).send_keys(card_data.card_1)
    mmyy = wdw(browser, 15).until(EC.presence_of_element_located(card_data_page_elements.card_date)).send_keys(card_data.mmyy_1)
    cvv = wdw(browser, 25).until(EC.presence_of_element_located(card_data_page_elements.cvv_num)).send_keys(card_data.cvv_1)
    card_buy_click = wdw(browser, 25).until(
        EC.presence_of_element_located(card_data_page_elements.card_buy_button)).click()
    paypass = wdw(browser, 20).until(EC.presence_of_element_located(cloud_page_elements.password_input)).send_keys(
        paypass_1)
    paypass_click = wdw(browser, 25).until(EC.presence_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 25).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))






