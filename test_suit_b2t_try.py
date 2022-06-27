from pageobject.methods_w_p import *
import pytest
from constance import *
import time


@pytest.mark.new_subjects
@pytest.mark.old_way
@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_head_page_elements_exists_b2c:

    def test_modern_byilogy_exist(self, browser):
        browser.get('https://57772.shot-uchi.ru/profile/students')
        browser.implicitly_wait(5)
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_bio"]')) == 1, 'biology button not exist, or more 1'

    def test_moder_literature_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_lit"]')) == 1, 'literature button not exist'

    def test_moder_geografy_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_geo"]')) == 1, 'literature button not exist'

    def test_moder_history_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_hist"]')) == 1, 'literature button not exist'


@pytest.mark.old_way
@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_shopping_year:

    def test_all_inclussive(self, browser):
        year = year_methods
        year.buy_all_inclusive(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.all_inclusive_congrat_button)).click()

    def test_math_year(self, browser):
        year = year_methods
        year.buy_math_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_year(self, browser):
        year = year_methods
        year.buy_math_rus_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_plan_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_plan_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_plan_bio_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_plan_bio_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_plan_bio_lit_year(self, browser):
        year = year_methods
        year.buy_math_rus_eng_prog_plan_bio_lit_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()


@pytest.mark.old_way
@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_shopping_half_year:

    def test_math_half_year(self, browser):
        halfyear = Half_year_methods
        halfyear.buy_math_half_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_half_year(self, browser):
        halfyear = Half_year_methods
        halfyear.buy_math_rus_half_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_half_year(self, browser):
        halfyear = Half_year_methods
        halfyear.buy_math_rus_eng_half_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_half_year(self, browser):
        halfyear = Half_year_methods
        halfyear.buy_math_rus_eng_prog_half_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_bio_half_year(self, browser):
        halfyear = Half_year_methods
        halfyear.buy_math_rus_eng_prog_bio_half_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_bio_lit_half_year(self, browser):
        halfyear = Half_year_methods
        halfyear.buy_math_rus_eng_prog_bio_lit_half_year(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()


@pytest.mark.old_way
@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_shopping_month:

    def test_math_month(self, browser):
        month = Month_methods
        month.buy_math_month(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_month(self, browser):
        month = Month_methods
        month.buy_math_rus_month(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_month(self, browser):
        month = Month_methods
        month.buy_math_rus_eng_month(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_month(self, browser):
        month = Month_methods
        month.buy_math_rus_eng_prog_month(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_bio_month(self, browser):
        month = Month_methods
        month.buy_math_rus_eng_prog_bio_month(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    def test_math_rus_eng_prog_bio_lit_month(self, browser):
        month = Month_methods
        month.buy_math_rus_eng_prog_bio_lit_month(self, browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
