from pageobject.methods import *
import pytest
from constance import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_head_page_elements_exists_b2t:

    def test_modern_byilogy_exist(self,browser):
        assert browser.find_elements_by_css_selector('[href="http://uchi.ru/modern-subjects/high-school/biology"]'), 'biology button not exist'


