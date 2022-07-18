from pageobject.methods import *
import pytest
from constance import *
import time
from flaky import flaky


@flaky
@pytest.mark.set_8th_b2t
@pytest.mark.regress
@pytest.mark.usefixtures('browser', 'authorization_b2t_8th')
class Test_head_page_elements_exists_b2t_8th:

    def test_modern_geography_exist(self, browser):
        browser.implicitly_wait(15)
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_geo"]')) == 1, 'geography button not exist'

    def test_modern_physics_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_phys"]')) == 1, 'physics button not exist'

    def test_modern_society_exist(self, browser):
        assert len(browser.find_elements_by_css_selector(
            '[data-qa-marker="content_soc"]')) == 1, 'society button not exist'


@flaky
@pytest.mark.set_8th_b2c
@pytest.mark.regress
@pytest.mark.usefixtures('browser', 'authorization_b2t_8th')
class Test_lk_new_subjects_exists:

    def test_lk_new_geography_exists(self, browser):
        browser.get('https://57772.shot-uchi.ru/profile/students/settings')
        browser.implicitly_wait(25)
        assert len(browser.find_elements(By.CSS_SELECTOR,
                                         '[data-qa-marker="discipline-modern_geography"]')) == 1, 'geography missing'

    def test_lk_new_physics(self, browser):
        assert len(browser.find_elements(By.CSS_SELECTOR,
                                         '[data-qa-marker="discipline-modern_physics"]')) == 1, 'physics missing'

    def test_lk_new_society(self, browser):
        assert len(browser.find_elements(By.CSS_SELECTOR,
                                         '[data-qa-marker="discipline-modern_social_science"]')) == 1, 'society missing'


@flaky
@pytest.mark.set_8th_b2t
@pytest.mark.regress
@pytest.mark.usefixtures('browser', 'authorization_b2t_8th')
class Test_high_school_buys_b2t_8th:

    @pytest.mark.new_code_try
    def test_buy_all_inclusive(self, browser):
        buy_all_inclusive(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.all_inclusive_congrat_button)).click()

    @pytest.mark.parametrize('checkboxes', new_subjects_8th)
    def test_modern_subjects_buy_year_8th(self, browser, checkboxes):
        new_subjects_year_8th(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(2)

    @pytest.mark.parametrize('old_checkboxes', old_subjects)
    def test_old_subjects_buy_year(self, browser, old_checkboxes):
        old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
        time.sleep(2)

    @pytest.mark.parametrize('checkboxes', new_subjects_8th)
    def test_modern_subjects_buy_half_year_8th(self, browser, checkboxes):
        new_subjects_halfyear_8th(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.parametrize('old_checkboxes', old_subjects_not_year)
    def test_old_subjects_buy_half_year(self, browser, old_checkboxes):
        old_subjects_halfyear(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.parametrize('checkboxes', new_subjects_8th)
    def test_modern_subjects_buy_month_8th(self, browser, checkboxes):
        new_subjects_month_8th(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()

    @pytest.mark.parametrize('old_checkboxes', old_subjects_not_year)
    def test_old_subjects_buy_month(self, browser, old_checkboxes):
        old_subjects_month(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
        congrat = 'https://57772.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'not correct page'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()
