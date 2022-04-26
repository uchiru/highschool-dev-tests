from pageobject.methods_w_p import *
import pytest
from constance import *
import time


@pytest.mark.set_new_b2c
@pytest.mark.regress
@pytest.mark.usefixtures('browser', 'avtorithaision_b2c')
class Test_head_page_elements_exists_b2c:

    def test_modern_byilogy_exist(self, browser):
        browser.implicitly_wait(5)
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_bio"]')) == 1, 'biology button not exist, or more 1'

    def test_moder_literature_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_lit"]')) == 1, 'literature button not exist'


@pytest.mark.set_new_b2c
@pytest.mark.usefixtures('browser', 'avtorithaision_b2c')
class Test_shopping_year:

    def test_all_inclussive(self, browser):
        year = year_methods
        year.buy_all_inclusive(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.all_inclusive_congrat_button)).click()

    def test_math_year(self, browser):
        year = year_methods
        year.buy_math_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_year(self, browser):
        year = year_methods
        year.buy_math_rus_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_plan_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_plan_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_plan_bio_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_plan_bio_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_plan_bio_lit_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_plan_bio_lit_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()