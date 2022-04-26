from pageobject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from constance import *
import time
import random
import string


class year_methods:

    def buy_all_inclusive(browser, card_1, mmyy_1, cvv_1, paypass_1):  # покупка все включено
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        all_inclusive_click = wdw(browser, 10).until(
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 30).until(
            EC.visibility_of_element_located(congrat_page_elements.all_inclusive_congrat_button))

    def buy_math_year(browser, card_1, mmyy_1, cvv_1, paypass_1):  # Покупка математики на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_year(browser, card_1, mmyy_1, cvv_1, paypass_1):  # покупка математики и русского на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_year(browser, card_1, mmyy_1, cvv_1,
                              paypass_1):  # покупка математики, русского и английского на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_year(browser, card_1, mmyy_1, cvv_1,
                                   paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
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
        paypass = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_plan_year(browser, card_1, mmyy_1, cvv_1,
                                        paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
        plan_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.plan_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_plan_bio_year(browser, card_1, mmyy_1, cvv_1,
                                            paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
        plan_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.plan_check_box)).click()
        bio_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_plan_bio_lit_year(browser, card_1, mmyy_1, cvv_1,
                                                paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
        plan_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.plan_check_box)).click()
        bio_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        lit_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))


class Half_year_methods:

    def buy_math_half_year(browser, card_1, mmyy_1, cvv_1, paypass_1):  # Покупка математики на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        gradusnick_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
        rus_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.rus_check_box)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_half_year(browser, card_1, mmyy_1, cvv_1, paypass_1):  # покупка математики и русского на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        gradusnick_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
        eng_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.eng_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_half_year(browser, card_1, mmyy_1, cvv_1,
                              paypass_1):  # покупка математики, русского и английского на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        gradusnick_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_half_year(browser, card_1, mmyy_1, cvv_1,
                                   paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        gradusnick_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
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
        paypass = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_bio_half_year(browser, card_1, mmyy_1, cvv_1,
                                       paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        gradusnick_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
        prog_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
        bio_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))

    def buy_math_rus_eng_prog_bio_lit_half_year(browser, card_1, mmyy_1, cvv_1,
                                                paypass_1):  # покупка математики, русского, английского и программирования на год
        browser.get('https://57211.shot-uchi.ru/profile/students')
        full_version = wdw(browser, 20).until(
            EC.visibility_of_element_located(headpage_elements.full_version_button)).click()
        gradusnick_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.gradusnik_halfyear)).click()
        prog_click = wdw(browser, 30).until(
            EC.visibility_of_element_located(payments_page_elements.prog_check_box)).click()
        bio_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_biology_check_box)).click()
        lit_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(payments_page_elements.modern_literature_check_box)).click()
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
            EC.visibility_of_element_located(cloud_page_elements.password_input)).send_keys(
            card_data.paypass_1)
        paypass_click = wdw(browser, 20).until(
            EC.visibility_of_element_located(cloud_page_elements.paypass_button)).click()
        paid_click = wdw(browser, 20).until(EC.visibility_of_element_located(congrat_page_elements.congrat_button))
