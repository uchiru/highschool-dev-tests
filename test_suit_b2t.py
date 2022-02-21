from pageobject.methods import *
import pytest
from constance import *
import time


@pytest.mark.usefixtures('browser', 'avtorithaision_b2t')
class Test_high_school_buys_b2t:

    @pytest.mark.parametrize('checkboxes', new_subjects)
    def test_modern_subjects_buy_year(self, browser, checkboxes):
        new_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        index = current_url.find(congrat)
        assert index != -1, 'not correct page'  # current_url == congrat, 'не та страница'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()


