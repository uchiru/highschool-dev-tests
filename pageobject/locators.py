from selenium.webdriver.common.by import By


class avtor_page_elements:
    login_input = (By.CSS_SELECTOR, '#login')
    password_input = (By.CSS_SELECTOR, '[id=password]')
    enter_button = (By.CSS_SELECTOR, '[value = "Войти"]')


class headpage_elements:
    full_version_button = (By.CSS_SELECTOR, '[data-testid="headbar-fullversion"]')


class payments_page_elements:
    geo_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_geo"]')
    history_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_history"]')
    modern_biology_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_biology"]')
    modern_literature_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_literature"]')
    physics_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_physics"]')
    society_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-modern_obshestvo"]')
    math_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-math"]')
    rus_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-russian"]')
    eng_check_box = (By.CSS_SELECTOR, '[data-qa-marker="product-name-english"]')
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
    subjects_list_button = (By.CSS_SELECTOR, '[style="margin-left: 6px;"]')
    bio_check = (By.CSS_SELECTOR, '[data-qa-marker="subject-id-32"]')
    lit_check = (By.CSS_SELECTOR, '[data-qa-marker="subject-id-36"]')
    geo_check = (By.CSS_SELECTOR, '[data-qa-marker="subject-id-9"]')
    hist_check = (By.CSS_SELECTOR, '[data-qa-marker="subject-id-13"]')
    save_check_button = (By.CSS_SELECTOR, '[data-qa-marker="submit-editable-class"]')
    header_head_page_button = (By.CSS_SELECTOR, 'a[href="https://57772.shot-uchi.ru/teachers/stats/main"]')
    student_list_pop_up_button = (By.XPATH, '//div[text()="Далее"]')
    your_class_hear_pop_up = (By.CSS_SELECTOR, '[data-qa-marker="main_page_new_btn"]')
    after_regist_pop_up_button = (By.CSS_SELECTOR, '[data-qa-marker="onboarding-button-next"]')
    biology_at_menu = (By.CSS_SELECTOR, '[data-qa-marker="menu-modern_biology"]')
    literature_at_menu = (By.CSS_SELECTOR, '[data-qa-marker="menu-modern_literature"]')
    group_list = (By.CSS_SELECTOR, '[data-name="classlist"]')
    class_settings_button = (
    By.CSS_SELECTOR, 'a[href="https://57772.shot-uchi.ru/teachers/class_books/1848357/students"]')
    marathon_pop_up = (By.CSS_SELECTOR, 'img.bottom_bar__marathon-hint')


class registraition_elements:
    regist_button = (By.CSS_SELECTOR, '[data-qa-marker="root-page-registration-link"]')
    teach_role_button = (By.CSS_SELECTOR, '[data-qa-marker="teacher-role"]')
    teach_email_box = (By.CSS_SELECTOR, '[data-qa-marker="step-email"]')
    teach_password_box = (By.CSS_SELECTOR, '[data-qa-marker="step-password"]')
    teach_privacy_check = (By.CSS_SELECTOR, '[data-qa-marker="checked-privacy"]')
    teach_email_letter_button = (By.CSS_SELECTOR, '[data-qa-marker="next-step-email-password"]')
    teach_last_name_box = (By.CSS_SELECTOR, '[data-qa-marker="step-lastName"]')
    teach_name_box = (By.CSS_SELECTOR, '[data-qa-marker="step-name"]')
    teach_middle_name_box = (By.CSS_SELECTOR, '[data-qa-marker="step-middleName"]')
    teach_phone_box = (By.CSS_SELECTOR, '[data-qa-marker="step-phone"]')
    teach_fio_letter_button = (By.CSS_SELECTOR, '[data-qa-marker="next-step-fio"]')
    teach_region_list = (By.CSS_SELECTOR, '[data-qa-marker="select-region"]')
    teach_region_name = (By.CSS_SELECTOR, '[data-qa-marker="Москва"]')
    teach_school_list = (By.CSS_SELECTOR, '[data-qa-marker="select-school"]')
    teach_school_name = (By.CSS_SELECTOR,
                         '[data-qa-marker="Государственное бюд3жетное общеобразовательное учреждение города Москвы средняя общеобразовательная школа №666"]')
    teach_school_later_button = (By.CSS_SELECTOR, '[data-qa-marker="next-step-school"]')
    teach_class_box = (By.CSS_SELECTOR, '[data-qa-marker="select-class-number"]')
    teach_class_level = (By.CSS_SELECTOR, '[data-qa-marker="5 класс"]')
    literature_checkbox = (By.CSS_SELECTOR, '[data-qa-marker="step-subject-id-36"]')
    biology_checbox = (By.CSS_SELECTOR, '[data-qa-marker="step-subject-id-32"]')
    teach_class_letter_button = (By.CSS_SELECTOR, '[data-qa-marker="next-step-add-class"]')
    option_biology_class = (By.CSS_SELECTOR, '[data-qa-marker="select-my-class-34"]')
    option_literature_class = (By.CSS_SELECTOR, '[data-qa-marker="select-my-class-38"]')
    class_option_letter_button = (By.CSS_SELECTOR, '[data-qa-marker="next-step-group-select"]')
