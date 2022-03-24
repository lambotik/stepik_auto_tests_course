from selenium import webdriver
import math
import time
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button1=browser.find_element_by_css_selector('.container .btn')
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    num=browser.find_element_by_id('input_value')
    x=num.text
    y=calc(x)
    answer= browser.find_element_by_id('answer')
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()