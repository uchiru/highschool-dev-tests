from selenium.webdriver.common.by import By


class avtor_page_elements:
    login_input = (By.CSS_SELECTOR, '#login')
    password_input = (By.CSS_SELECTOR, '[id=password]')
    enter_button = (By.CSS_SELECTOR, '[value = "Войти"]')


class headpage_elements:
    full_version_button = (By.CSS_SELECTOR, '[data-testid="headbar-fullversion"]')


class payments_page_elements:
    modern_biology_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_biology"]')
    modern_literature_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_literature"]')
    math_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-math"]')
    rus_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-russian"]')
    eng_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-english"]')
    env_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-environment"]')
    prog_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-informatics"]')
    plan_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-plan"]')
    buy_button = (By.CSS_SELECTOR, '[data-qa-marker ="buy-selected-products"]')
    gradusnik_halfyear = (By.CSS_SELECTOR, '[data-qa-marker ="полгода"]')
    gradusnik_month = (By.CSS_SELECTOR, '[data-qa-marker ="месяц"]')
    all_inclusive_button = (By.CSS_SELECTOR, '[data-qa-marker="buy-bundle"]')


class card_data_page_elements:
    card_num = (By.CSS_SELECTOR, 'input#cardNumber')
    card_date = (By.ID, 'expDateMonthYear')
    cvv_num = (By.ID, 'cvv')
    card_buy_button = (By.CSS_SELECTOR, '[data-qa-marker ="submit"]')


class cloud_page_elements():
    password_input = (By.CSS_SELECTOR, '[id=password]')
    paypass_button = (By.CSS_SELECTOR, '[type="submit"]')


class congrat_page_elements():
    congrat_button = (By.CSS_SELECTOR, 'a.paid__btn')
    all_inclusive_congrat_button = (By.CSS_SELECTOR, 'a.btn.btn-blue')


class teachers_elements:
    subjects_list_button = (By.CSS_SELECTOR, '[data-qa-marker="edit-subjects"]')
    bio_check = (By.CSS_SELECTOR, '[data-qa-marker="subject-id-32"]')
    lit_check = (By.CSS_SELECTOR, '[data-qa-marker="subject-id-36"]')
    save_check_button = (By.CSS_SELECTOR, '[data-qa-marker="submit-editable-class"]')
    header_head_page_button = (By.CSS_SELECTOR, 'a[href="https://57211.shot-uchi.ru/teachers/stats/main"]')
    blyadskiy_pop_up_button = (By.XPATH, '//div[text()="Далее"]')


class registraition_elements:
    regist_button = (By.CSS_SELECTOR, '[data-qa-marker="root-page-registration-link"]')
    teach_role_button = (By.CSS_SELECTOR, '[data-qa-marker="teacher-role"]')
    teach_email_box = (By.CSS_SELECTOR, '[data-qa-marker="step-email"]')
    teach_password_box = (By.CSS_SELECTOR, '[data-qa-marker="step-password"]')
    teach_privacy_check = (By.CSS_SELECTOR, '[data-qa-marker="checked-privacy"]')
    teach_email_letter_button = (By.CSS_SELECTOR, '[data-qa-marker="next-step-email-password"]')

