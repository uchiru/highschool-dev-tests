from pageobject.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC
from constance import subject
import time
from datetime import *

loginx = 'admin+admin@uchi.ru'
passwordx = '1'
login_1 = '141'
password_1 = '19468персик'  # ученик https://56026.shot-uchi.ru/admin/students/20779933
login_2 = '31'
password_2 = 'певец12481'  # ученик https://56026.shot-uchi.ru/admin/students/20309696
card_1 = '4242 4242 4242 4242'
mmyy_1 = '12/22'
cvv_1 = '111'
paypass_1 = '4'


#def avtorithaision(browser, login, password):
 #   browser.get('https://56026.shot-uchi.ru/')
  #  login_input = wdw(browser, 15).until(EC.presence_of_element_located(usingelements.login_input)).send_keys(login)
   # password_input = wdw(browser, 35).until(EC.presence_of_element_located(usingelements.password_input)).send_keys(
    #    password)
    #enter = wdw(browser, 15).until(EC.presence_of_element_located(usingelements.enter_button)).click()

def new_biology_year(browser, card_1, mmyy_1, cvv_1, paypass_1):
    full_version = wdw(browser, 30).until(EC.presence_of_element_located(usingelements.full_version_button)).click()
    modern_biology_click = wdw(browser, 30).until(EC.presence_of_element_located(subjects_checkbox.modern_biology_check_box)).click()
    buy_click = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.buy_button)).click()
    card = wdw(browser, 15).until(EC.presence_of_element_located(usingelements.card_num)).send_keys(card_1)
    mmyy = wdw(browser, 15).until(EC.presence_of_element_located(usingelements.card_date)).send_keys(mmyy_1)
    cvv = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.cvv_num)).send_keys(cvv_1)
    card_buy_click = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.card_buy_button)).click()
    paypass = wdw(browser, 20).until(EC.presence_of_element_located(usingelements.password_input)).send_keys(paypass_1)
    paypass_click = wdw(browser, 25).until(EC.presence_of_element_located(usingelements.paypass_button)).click()
    paid_click = wdw(browser, 25).until(EC.visibility_of_element_located(usingelements.paid_btn))
