from conftest import browser
from pageobject.methods import *
import pytest
from constance import *
import time


@pytest.mark.usefixtures('browser', 'avtorithaision')
class Test_high_school_buys_b2t:

    @pytest.mark.parametrize('checkboxes', subject)
    def test_modern_biology_buy_year(self, browser, checkboxes):
        new_biology_year(browser, card_1, mmyy_1, cvv_1, paypass_1, checkboxes)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'не та страница'
        congrat_button_click = wdw(browser, 10).until(
            EC.presence_of_element_located(usingelements.congrat_button)).click()
