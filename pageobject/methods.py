from pageobject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from constance import subject
import time
from datetime import *

loginx = 'admin+admin@uchi.ru'
passwordx = '1'
login_1 = '141'
password_1 = '19468персик'  # ученик https://56026.shot-uchi.ru/admin/students/20779933
login_2 = '31'
password_2 = 'певец12481'  # ученик https://56026.shot-uchi.ru/admin/students/20309696
card_1 = '4242 4242 4242 4242'
mmyy_1 = '12/22'
cvv_1 = '111'
paypass_1 = '4'


def skip_over_checkbox(browser):
    math_biology_click = wdw(browser, 20).until(
        EC.presence_of_element_located(subjects_checkbox.math_check_box)).click()
    rus_biology_click = wdw(browser, 20).until(EC.presence_of_element_located(subjects_checkbox.rus_check_box)).click()
    modern_biology_click = wdw(browser, 20).until(
        EC.presence_of_element_located(subjects_checkbox.eng_check_box)).click()


def new_biology_year(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox):
    full_version = wdw(browser, 30).until(EC.presence_of_element_located(usingelements.full_version_button)).click()
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 30).until(
            EC.presence_of_element_located(subjects_checkbox.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 30).until(
            EC.presence_of_element_located(subjects_checkbox.modern_literature_check_box)).click()
    else:
        modern_biology_click = wdw(browser, 30).until(
            EC.presence_of_element_located(subjects_checkbox.modern_biology_check_box)).click()
        literature_click = wdw(browser, 30).until(
            EC.presence_of_element_located(subjects_checkbox.modern_literature_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.buy_button)).click()
    card = wdw(browser, 15).until(EC.presence_of_element_located(usingelements.card_num)).send_keys(card_1)
    mmyy = wdw(browser, 15).until(EC.presence_of_element_located(usingelements.card_date)).send_keys(mmyy_1)
    cvv = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.cvv_num)).send_keys(cvv_1)
    card_buy_click = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.card_buy_button)).click()
    paypass = wdw(browser, 20).until(EC.presence_of_element_located(usingelements.password_input)).send_keys(paypass_1)
    paypass_click = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.paypass_button)).click()
    paid_click = wdw(browser, 25).until(EC.visibility_of_element_located(usingelements.paid_btn))
