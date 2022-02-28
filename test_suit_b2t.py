from pageobject.methods import *
import pytest
from constance import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_high_school_buys_b2t:

    @pytest.mark.parametrize('checkboxes', new_subjects)
    def test_modern_subjects_buy_year(self, browser, checkboxes):
        new_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.parametrize('old_checkboxes', old_subjects)
    def test_old_subjects_buy_year(self, browser, old_checkboxes):
        old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.new_code_try
    @pytest.mark.parametrize('checkboxes', new_subjects)
    def test_modern_subjects_buy_half_year(self, browser, checkboxes):
        new_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.new_code_try
    @pytest.mark.parametrize('old_checkboxes', old_subjects_not_year)
    def test_old_subjects_buy_half_year(self, browser, old_checkboxes):
        old_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.parametrize('checkboxes', new_subjects)
    def test_modern_subjects_buy_month(self, browser, checkboxes):
        new_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.new_code_try
    @pytest.mark.parametrize('old_checkboxes', old_subjects_not_year)
    def test_old_subjects_buy_month(self, browser, old_checkboxes):
        old_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

