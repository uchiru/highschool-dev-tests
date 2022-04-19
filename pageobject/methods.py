from pageobject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from constance import *
import time


def skip_over_checkbox(browser):
    math_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
    rus_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    eng_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()


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
    else:
        modern_biology_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
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
    paypass = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
        card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    if choose_check_box == 'math':
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'rus':
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
    elif choose_check_box == 'eng':
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'prog':
        prog_click = wdw(browser, 20).until(
            (EC.visibility_of_element_located(payments_page_elements.prog_check_box))).click()
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'plan':
        plan_click = wdw(browser, 20).until(
            (EC.visibility_of_element_located(payments_page_elements.plan_check_box))).click()
        math_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    else:
        plan_click = wdw(browser, 20).until(
            (EC.visibility_of_element_located(payments_page_elements.plan_check_box))).click()
        prog_click = wdw(browser, 20).until(
            (EC.visibility_of_element_located(payments_page_elements.prog_check_box))).click()
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
    paypass = wdw(browser, 40).until(EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
        card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
    if choose_checkbox == 'bio':
        browser.implicitly_wait(5)
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    else:
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
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
    paypass = wdw(browser, 40).until(EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
        card_data.paypass_1)
    paypass_click = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def old_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
    if choose_check_box == 'math':
        rus_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'rus':
        math_click = wdw(browser, 35).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        eng_click = wdw(browser, 35).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'eng':
        math_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'prog':
        math_click = wdw(browser, 30).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 30).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 30).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
        prog_click = wdw(browser, 30).until(
            (EC.visibility_of_element_located(payments_page_elements.prog_check_box))).click()
    elif choose_check_box == 'all_types':
        prog_click = wdw(browser, 25).until(
            (EC.visibility_of_element_located(payments_page_elements.prog_check_box))).click()
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
    paypass_click = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def new_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_checkbox):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_month)).click()
    if choose_checkbox == 'bio':
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
    elif choose_checkbox == 'lit':
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
    else:
        modern_biology_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        literature_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
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
    paypass_click = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def old_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 20).until(
        EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
    gradusnick_click = wdw(browser, 20).until(
        EC.visibility_of_element_located(payments_page_elements.gradusnik_month)).click()
    if choose_check_box == 'math':
        browser.implicitly_wait(5)
        rus_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    elif choose_check_box == 'rus':
        eng_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
        math_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
    elif choose_check_box == 'eng':
        math_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'prog':
        prog_click = wdw(browser, 25).until(
            (EC.visibility_of_element_located(payments_page_elements.prog_check_box))).click()
        math_click = wdw(browser, 30).until(
            EC.visibility_of_element_located(payments_page_elements.math_check_box)).click()
        rus_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 25).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
    else:
        prog_click = wdw(browser, 25).until(
            (EC.visibility_of_element_located(payments_page_elements.prog_check_box))).click()
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
    paypass_click = wdw(browser, 20).until(EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
    paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


def teach_sub_management(browser, choose_subjects):
    browser.get('https://57211.shot-uchi.ru/teachers/lk/main')
    subjects_list = wdw(browser, 20).until(EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
    if choose_subjects == 'bio':
        bio_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.bio_check)).click()
    elif choose_subjects == 'lit':
        lit_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.lit_check)).click()
    else:
        bio_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.bio_check)).click()
        lit_choose = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.lit_check)).click()
    save_change_click = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
    try:
        continue_button = wdw(browser,15).until(EC.visibility_of_element_located(teachers_elements.blyadskiy_pop_up_button)).click()
    except:
        print("Pop up lose")
    time.sleep(5)
    header_click = wdw(browser, 15).until(EC.visibility_of_element_located(teachers_elements.header_head_page_button)).click()
    time.sleep(5)
