from selenium import webdriver
import math
import time
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button1=browser.find_element_by_css_selector('.container .trollface')
    button1.click()
    new_window = browser.window_handles[1] #узнаем имя новой вкладки
    first_window = browser.window_handles[0] #запоминаем имя первой вкладки
    browser.switch_to.window(new_window) #переключаем браузер на новую вкладку
    num=browser.find_element_by_id('input_value')
    x=num.text
    y=calc(x)
    answer= browser.find_element_by_id('answer')
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(999)
    browser.quit()