from pageobject.methods import *
import pytest
from constance import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('browser', 'avtorithaision_techear')
class Test_teacher_sub_management:

    @pytest.mark.regress
    @pytest.mark.teach_set
    @pytest.mark.parametrize('checkboxes', teach_subjects)
    def test_sub_management(self, browser, checkboxes):
        teach_sub_management(browser, checkboxes)
        if checkboxes == 'bio':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-modern_biology"]')) == 0, 'biology missing at progrrams list'
        elif checkboxes == 'lit':
            assert len(browser.find_elements_by_css_selector(
                '[data-qa-marker="menu-modern_literature"]')) == 0, 'literature missing at programs list'
        # elif checkboxes == 'geo':
        #     assert len(browser.find_elements_by_css_selector(
        #         '[data-qa-marker="menu-modern_geography"]')) == 0, 'literature missing at programs list'
        # elif checkboxes == 'hist':
        #     assert len(browser.find_elements_by_css_selector(
        #         '[data-qa-marker="menu-modern_history"]')) == 0, 'literature missing at programs list'
        else:
            assert len(browser.find_elements_by_css_selector('[data-qa-marker="menu-modern_biology"]')) == 1 and len(
                browser.find_elements_by_css_selector('[data-qa-marker="menu-modern_literature"]')) == 1 #and len(
                # browser.find_elements_by_css_selector('[data-qa-marker="menu-modern_geography"]')) == 1 and len(
                # browser.find_elements_by_css_selector('[data-qa-marker="menu-modern_history"]')) == 1, 'some new subject missing at progrrams list'


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
