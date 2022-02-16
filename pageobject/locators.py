from selenium.webdriver.common.by import By


class usingelements():
    login_input = (By.CSS_SELECTOR, '#login')
    password_input = (By.CSS_SELECTOR, '[id=password]')
    enter_button = (By.CSS_SELECTOR, '[value = "Войти"]')
    full_version_button = (By.CSS_SELECTOR, '[data-testid="headbar-fullversion"]')
    card_num = (By.ID, 'cardNumber')
    buy_button = (By.CSS_SELECTOR, '[data-qa-marker ="buy-selected-products"]')
    all_inclusive_buy_button = (By.CSS_SELECTOR, '[data-qa-marker="buy-bundle"]')
    card_date = (By.ID, 'expDateMonthYear')
    cvv_num = (By.ID, 'cvv')
    card_buy_button = (By.CSS_SELECTOR, '[data-qa-marker ="submit"]')
    paid_btn = (By.CSS_SELECTOR, 'a.paid__btn')
    paypass_button = (By.CSS_SELECTOR, '.btn')
    congrat_button = (By.CLASS_NAME, 'paid__btn')


class subjects_checkbox():
    modern_biology_check_box = (By.XPATH, '//span[text()="Modern Биология"]')
    modern_literature_check_box = (By.XPATH, '//span[text()="Литература"]')
    math_check_box = (By.XPATH, '//span[text()="Математика"]')
    rus_check_box = (By.XPATH, '//span[text()="Русский язык"]')
    eng_check_box = (By.XPATH, '//span[text()="Английский язык"]')
