from pageobject.methods import *
import pytest
from constance import *
import time


@pytest.mark.set_b2c
@pytest.mark.regress
@pytest.mark.usefixtures('browser', 'avtorithaision_b2c_7th')
class Test_head_page_elements_exists_b2c_7th:

    def test_modern_byilogy_exist(self, browser):
        browser.implicitly_wait(15)
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_bio"]')) == 1, 'biology button not exist, or more 1'

    def test_moder_literature_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_lit"]')) == 1, 'literature button not exist'

    def test_moder_geography_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_geo"]')) == 1, 'geography button not exist'

    def test_moder_physics_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_phys"]')) == 1, 'physics button not exist'

    def test_moder_society_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_soc"]')) == 1, 'society button not exist'


@pytest.mark.set_b2c
@pytest.mark.regress
@pytest.mark.usefixtures('browser', 'avtorithaision_b2c_7th')
class Test_high_school_buys_b2c_7th:

    @pytest.mark.new_code_try
    def test_buy_all_inclusive(self, browser):
        buy_all_inclusive(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.all_inclusive_congrat_button)).click()

    @pytest.mark.parametrize('checkboxes', new_subjects_7th)
    def test_modern_subjects_buy_year_7th(self, browser, checkboxes):
        new_subjects_year_7th(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(5)

    @pytest.mark.parametrize('old_checkboxes', old_subjects)
    def test_old_subjects_buy_year(self, browser, old_checkboxes):
        old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(5)

    @pytest.mark.parametrize('checkboxes', new_subjects_7th)
    def test_modern_subjects_buy_half_year_7th(self, browser, checkboxes):
        new_subjects_halfyear_7th(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(5)

    @pytest.mark.b2c_half_year
    @pytest.mark.parametrize('old_checkboxes', old_subjects_not_year)
    def test_old_subjects_buy_half_year(self, browser, old_checkboxes):
        old_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(5)

    @pytest.mark.parametrize('checkboxes', new_subjects_7th)
    def test_modern_subjects_buy_month_7th(self, browser, checkboxes):
        new_subjects_month_7th(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(5)

    @pytest.mark.parametrize('old_checkboxes', old_subjects_not_year)
    def test_old_subjects_buy_month(self, browser, old_checkboxes):
        old_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(5)