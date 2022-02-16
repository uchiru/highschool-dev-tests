from pageobject.methods import *
import pytest


@pytest.mark.usefixture("browser", "avtorithaision")
class Test_high_school_buys_b2t:
    def test_modern_biology_buy_year(self, browser):
        new_biology_year(browser, card_1, mmyy_1, cvv_1, paypass_1)
        congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
        current_url = browser.current_url
        assert current_url == congrat, 'не та страница'
