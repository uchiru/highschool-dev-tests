from selenium.webdriver.common.by import By


class avtor_page_elements():
    login_input = (By.CSS_SELECTOR, '#login')
    password_input = (By.CSS_SELECTOR, '[id=password]')
    enter_button = (By.CSS_SELECTOR, '[value = "Войти"]')


class subjects_checkbox():
    modern_biology_check_box = (By.XPATH, '//span[text()="Modern Биология"]')
    modern_literature_check_box = (By.XPATH, '//span[text()="Литература"]')
    math_check_box = (By.XPATH, '//span[text()="Математика"]')
    rus_check_box = (By.XPATH, '//span[text()="Русский язык"]')
    eng_check_box = (By.XPATH, '//span[text()="Английский язык"]')


class headpage_elements():
    full_version_button = (By.CSS_SELECTOR, '[data-testid="headbar-fullversion"]')


class payments_page_elements():
    modern_biology_check_box = (By.XPATH, '//span[text()="Modern Биология"]')
    modern_literature_check_box = (By.XPATH, '//span[text()="Литература"]')
    math_check_box = (By.XPATH, '//span[text()="Математика"]')
    rus_check_box = (By.XPATH, '//span[text()="Русский язык"]')
    eng_check_box = (By.XPATH, '//span[text()="Английский язык"]')
    prog_check_box = (By.XPATH,'//span[text()="Программирование"]')
    plan_check_box = (By.XPATH,'//span[text()="Планирование"]')
    buy_button = (By.CSS_SELECTOR, '[data-qa-marker ="buy-selected-products"]')


class card_data_page_elements():
    card_num = (By.ID, 'cardNumber')
    card_date = (By.ID, 'expDateMonthYear')
    cvv_num = (By.ID, 'cvv')
    card_buy_button = (By.CSS_SELECTOR, '[data-qa-marker ="submit"]')


class cloud_page_elements():
    password_input = (By.CSS_SELECTOR, '[id=password]')
    paypass_button = (By.CSS_SELECTOR, '[type="submit"]')


class congrat_page_elements():
    congrat_button = (By.CSS_SELECTOR, 'a.paid__btn')




