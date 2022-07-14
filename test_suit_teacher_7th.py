from pageobject.methods import *
import pytest
from constance import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from flaky import flaky
from pageobject.locators import *


@flaky
@pytest.mark.usefixtures('browser', 'avtorithaision_techear_7th')
class Test_teacher_7th_sub_management:

    @pytest.mark.regress
    @pytest.mark.teach_set7
    @pytest.mark.parametrize('checkboxes', teach_subjects_7th)
    def test_7th_sub_management(self, browser, checkboxes):
        if len(browser.find_elements(By.CSS_SELECTOR, '[data-qa-marker="menu-modern_biology"]')) == 0 and \
                checkboxes == 'bio':
            subjects_list = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
            bio_choose = wdw(browser, 30).until(EC.visibility_of_element_located(teachers_elements.bio_check)).click()
            target = browser.find_element_by_css_selector(
                '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
            save_change_click = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
            browser.get('https://57772.shot-uchi.ru/teachers/lk/main')
        elif len(browser.find_elements(By.CSS_SELECTOR, '[data-qa-marker="menu-modern_literature"]')) == 0 and \
                checkboxes == 'lit':
            subjects_list = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
            lit_choose = wdw(browser, 30).until(EC.visibility_of_element_located(teachers_elements.lit_check)).click()
            target = browser.find_element_by_css_selector(
                '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
            save_change_click = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
            browser.get('https://57772.shot-uchi.ru/teachers/lk/main')
        elif len(browser.find_elements(By.CSS_SELECTOR, '[data-qa-marker="menu-geo"]')) == 0 and \
                checkboxes == 'geo':
            subjects_list = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
            geo_choose = wdw(browser, 30).until(EC.visibility_of_element_located(teachers_elements.geo_check)).click()
            target = browser.find_element_by_css_selector(
                '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
            save_change_click = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
            browser.get('https://57772.shot-uchi.ru/teachers/lk/main')
        elif len(browser.find_elements(By.CSS_SELECTOR, '[data-qa-marker="menu-phys"]')) == 0 and \
                checkboxes == 'phys':
            subjects_list = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
            phys_choose = wdw(browser, 30).until(EC.visibility_of_element_located(teachers_elements.phys_check)).click()
            target = browser.find_element_by_css_selector(
                '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
            save_change_click = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
            browser.get('https://57772.shot-uchi.ru/teachers/lk/main')
        elif len(browser.find_elements(By.CSS_SELECTOR, '[data-qa-marker="menu-soc"]')) == 0 and \
                checkboxes == 'soc':
            subjects_list = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.subjects_list_button)).click()
            soc_choose = wdw(browser, 30).until(EC.visibility_of_element_located(teachers_elements.soc_check)).click()
            target = browser.find_element_by_css_selector(
                '[data-qa-marker="submit-editable-class"]').location_once_scrolled_into_view
            save_change_click = wdw(browser, 30).until(
                EC.visibility_of_element_located(teachers_elements.save_check_button)).click()
            browser.get('https://57772.shot-uchi.ru/teachers/lk/main')
        teach_sub_management_7th(browser, checkboxes)
        if checkboxes == 'bio':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-modern_biology"]')) == 0, 'biology missing at progrrams list'
        elif checkboxes == 'lit':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-modern_literature"]')) == 0, 'literature missing at programs list'
        elif checkboxes == 'geo':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-geo"]')) == 0, 'geography missing at programs list'
        elif checkboxes == 'phys':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-phys"]')) == 0, 'physics missing at programs list'
        elif checkboxes == 'soc':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-soc"]')) == 0, 'sociology missing at programs list'
        elif checkboxes == 'all_checks':
            assert len(browser.find_elements_by_css_selector('[data-qa-marker="menu-modern_biology"]')) == 1 and len(
                browser.find_elements_by_css_selector('[data-qa-marker="menu-modern_literature"]')) == 1 and len(
                browser.find_elements_by_css_selector('[data-qa-marker="menu-geo"]')) == 1 and len(
                browser.find_elements_by_css_selector('[data-qa-marker="menu-phys"]')) == 1 and len(
                browser.find_elements_by_css_selector('[data-qa-marker="menu-soc"]')) == 1, 'some new subject missing at progrrams list'


# class Test_teacher_with_registration:
#
#     @pytest.mark.regress
#     @pytest.mark.teach_set
#     @pytest.mark.teach
#     def test_choose_exists_classes(self, browser):
#         regist_and_choose_classes(browser)
#         empty_name = browser.find_element_by_css_selector('[data-qa-marker="add-student-last-name"]').text
#         print(empty_name)
#         assert empty_name == '', "not empty group"
