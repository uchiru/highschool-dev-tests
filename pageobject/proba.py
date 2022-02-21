@pytest.mark.parametrize('old_checkboxes', old_subjects)
def test_old_subjects_buy_year(self, browser, select_checkboxes):
    old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, old_checkboxes)
    congrat = 'https://57211.shot-uchi.ru/students/payments/complete'
    current_url = browser.current_url
    index = current_url.find(congrat)
    assert index != -1, 'not correct page'  # current_url == congrat, 'не та страница'
    congrat_button_click = wdw(browser, 10).until(
        EC.presence_of_element_located(congrat_page_elements.congrat_button)).click()


class old_subjects_year(browser, card_1, mmyy_1, cvv_1, paypass_1, choose_check_box):
    browser.get('https://57211.shot-uchi.ru/profile/students')
    full_version = wdw(browser, 30).until(EC.presence_of_element_located(headpage_elements.full_version_button)).click()
    skip_over_checkbox(browser)
    if choose_check_box == 'math':
        math_click = wdw(browser, 10).until(EC.presence_of_element_located(payments_page_elements.math_check_box)).click()
    elif choose_check_box == 'rus':
        rus_click = wdw(browser, 10).until(
            EC.presence_of_element_located(payments_page_elements.rus_check_box)).click()
    elif choose_check_box == 'eng':
        eng_click = math_click = wdw(browser, 10).until(EC.presence_of_element_located(payments_page_elements.eng_check_box)).click()