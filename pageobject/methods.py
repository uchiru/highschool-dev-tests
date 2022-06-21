from pageobject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from constance import *
import time
import random
import string


def generate_email(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    email = (f'{rand_string}@gmail.com')
    return email


def skip_over_checkbox(browser):
    math_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
    rus_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    eng_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()


def buy_all_inclusive(browser, card_1, mmyy_1, cvv_1, paypass_1):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    choose_all_inclusive = wdw(browser, 15).until(
        EC.visibility_of_element_located(payments_page_elements.all_inclusive_button)).click()
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(congrat_page_elements.all_inclusive_congrat_button))


def new_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    elif choose_checkbox == 'hist':
        history_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.history_check_box)).click()
    elif choose_checkbox == 'geo':
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    elif choose_checkbox == 'all_types':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
        history_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.history_check_box)).click()
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_year_7th(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    elif choose_checkbox == 'soc':
        society_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.society_check_box)).click()
    elif choose_checkbox == 'phys':
        phys_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.physics_check_box)).click()
    elif choose_checkbox == 'geo':
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    elif choose_checkbox == 'all_types':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
        society_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.society_check_box)).click()
        phys_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.physics_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box): # ученик старые предметы
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    if choose_check_box == 'math':
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'rus':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'eng':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'prog':
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'plan':
        plan_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.plan_check_box)).click()
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    else:
        plan_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.plan_check_box)).click()
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(10)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 40).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox): # Ученик 5й класс
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
    browser.implicitly_wait(10)
    if choose_checkbox == 'bio':
        browser.implicitly_wait(5)
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    elif choose_checkbox == 'hist':
        history_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.history_check_box)).click()
    elif choose_checkbox == 'geo':
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    elif choose_checkbox == 'all_types':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
        history_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.history_check_box)).click()
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(10)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 40).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_halfyear_7th(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox): # Ученик 7й класс
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
    browser.implicitly_wait(10)
    if choose_checkbox == 'bio':
        browser.implicitly_wait(5)
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    elif choose_checkbox == 'soc':
        society_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.society_check_box)).click()
    elif choose_checkbox == 'phys':
        phys_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.physics_check_box)).click()
    elif choose_checkbox == 'geo':
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    elif choose_checkbox == 'all_types':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
        society_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.society_check_box)).click()
        phys_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.physics_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def old_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box): # ученик старые предметы
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
    browser.implicitly_wait(10)
    if choose_check_box == 'math':
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'rus':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'eng':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'prog':
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
    else:
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 40).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox): # ученик 5й класс
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_month)).click()
    browser.implicitly_wait(10)
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    elif choose_checkbox == 'hist':
        history_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.history_check_box)).click()
    elif choose_checkbox == 'geo':
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    elif choose_checkbox == 'all_types':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
        history_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.history_check_box)).click()
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 40).until(EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
        card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_month_7th(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox): # ученик 7йкласс
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_month)).click()
    browser.implicitly_wait(10)
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    elif choose_checkbox == 'soc':
        society_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.society_check_box)).click()
    elif choose_checkbox == 'phys':
        phys_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.physics_check_box)).click()
    elif choose_checkbox == 'geo':
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    elif choose_checkbox == 'all_types':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
        geo_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.geo_check_box)).click()
    skip_over_checkbox(browser)
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 40).until(EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
        card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def old_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box): #Ученик-старые предметы
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_month)).click()
    browser.implicitly_wait(10)
    if choose_check_box == 'math':
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'rus':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'eng':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'prog':
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
    else:
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
    buy_click = wdw(browser, 20).until(EC.visibility_of_element_located(payments_page_elements.buy_button)).click()
    browser.implicitly_wait(15)
    card = wdw(browser, 40).until(EC.visibility_of_element_located(card_data_page_elements.card_num)).send_keys(
        card_data.card_1)
    mmyy = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.card_date)).send_keys(
        card_data.mmyy_1)
    cvv = wdw(browser, 20).until(EC.visibility_of_element_located(card_data_page_elements.cvv_num)).send_keys(
        card_data.cvv_1)
    card_buy_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(card_data_page_elements.card_buy_button)).click()
    browser.implicitly_wait(10)
    paypass = wdw(browser, 40).until(
        EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def teach_sub_management(browser, choose_subjects):  #учитель-5й класс
    browser.get('https://57211.shot-uchi.ru/teachers/lk/main')
    subjects_list = wdw(browser, 20).until(
        EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
    if choose_subjects == 'bio':
        bio_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.bio_check)).click()
    # elif choose_subjects == 'geo':
    #     geo_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.geo_check)).click()
    # elif choose_subjects == 'hist':
    #     hist_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.hist_check)).click()
    elif choose_subjects == 'lit':
        lit_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.lit_check)).click()
    else:
        bio_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.bio_check)).click()
        lit_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.lit_check)).click()
        # geo_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.geo_check)).click()
        # hist_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.hist_check)).click()
    target = browser.find_element_by_css_selector(
        '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
    save_change_click = wdw(browser, 15).until(
        EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
    try:
        continue_button = wdw(browser, 15).until(
            EC.visibility_of_element_located(teachers_elements.student_list_pop_up_button)).click()
    except:
        print("Pop up lose")
    header_click = wdw(browser, 15).until(
        EC.visibility_of_element_located(teachers_elements.header_head_page_button)).click()
    browser.implicitly_wait(5)


def regist_and_choose_classes(browser):     #учитель-5й класс
    browser.get('https://57211.shot-uchi.ru')
    regist_click = wdw(browser, 10).until(
        EC.visibility_of_element_located(registraition_elements.regist_button)).click()
    choose_role_button = wdw(browser, 10).until(
        EC.visibility_of_element_located(registraition_elements.teach_role_button)).click()
    teach_email_input = wdw(browser, 10).until(
        EC.visibility_of_element_located(registraition_elements.teach_email_box)).send_keys(generate_email(7))
    teach_password_input = wdw(browser, 10).until(
        EC.visibility_of_element_located(registraition_elements.teach_password_box)).send_keys('11111111')
    checkbox = wdw(browser, 10).until(EC.visibility_of_element_located(registraition_elements.teach_privacy_check))
    browser.execute_script('return console.log(arguments[0]);', checkbox)
    browser.execute_script('return arguments[0].innerText = "sdfsdfsdfds";', checkbox)
    teach_agree_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_privacy_check)).click()
    teach_email_letter_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_email_letter_button)).click()
    teach_name_input = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_name_box)).send_keys('Чувак')
    teach_last_name_input = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_last_name_box)).send_keys('Чуваков')
    teach_middle_name_input = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_middle_name_box)).send_keys('Чувакович')
    teach_phone_input = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_phone_box)).click()
    teach_phone_input = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_phone_box)).send_keys('1111111111')
    teach_fio_letter_button = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_fio_letter_button)).click()
    teach_region_select = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_region_list)).click()
    teach_region_option = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_region_name)).click()
    teach_school_click = wdw(browser, 10).until(
        EC.visibility_of_element_located(registraition_elements.teach_school_list)).click()
    teach_school_send = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_school_list)).send_keys('666')
    teach_school_option = wdw(browser, 45).until(
        EC.visibility_of_element_located(registraition_elements.teach_school_name)).click()
    target = browser.find_element_by_css_selector(
        '[data-qa-marker="next-step-school"]').location_once_scrolled_into_view
    teach_school_letter_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_school_later_button)).click()
    teach_class_level = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_class_box)).click()
    teach_class_level_option = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_class_level)).click()
    literature_option = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.literature_checkbox)).click()
    biology_option = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.biology_checbox)).click()
    teach_class_letter_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.teach_class_letter_button)).click()
    biology_group_option = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.option_biology_class)).click()
    target = browser.find_element_by_css_selector(
        '[data-qa-marker="select-my-class-38"]').location_once_scrolled_into_view
    literature_group_option = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.option_literature_class)).click()
    target = browser.find_element_by_css_selector(
        '[data-qa-marker="next-step-group-select"]').location_once_scrolled_into_view
    group_option_letter_button = wdw(browser, 20).until(
        EC.visibility_of_element_located(registraition_elements.class_option_letter_button)).click()
    browser.implicitly_wait(20)
    try:
        continue_button = wdw(browser, 15).until(
            EC.visibility_of_element_located(teachers_elements.your_class_hear_pop_up)).click()
    except:
        print("Pop up lose")
    have_biology = wdw(browser, 20).until(EC.visibility_of_element_located(teachers_elements.biology_at_menu))
    have_literature = wdw(browser, 20).until(EC.visibility_of_element_located(teachers_elements.literature_at_menu))
    subjects_list = wdw(browser, 20).until(
        EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
    target = browser.find_element_by_css_selector(
        '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
    try:
        marathon_button = wdw(browser, 15).until(
            EC.visibility_of_element_located(teachers_elements.marathon_pop_up)).click()
    except:
        print("Pop up lose")
    save_change_click = wdw(browser, 15).until(
        EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
    try:
        continue_button = wdw(browser, 15).until(
            EC.visibility_of_element_located(teachers_elements.student_list_pop_up_button)).click()
    except:
        print("Pop up lose")

