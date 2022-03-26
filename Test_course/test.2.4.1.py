import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button=WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button1=browser.find_element_by_id("book")
    button1.click()
    num = browser.find_element_by_id('input_value')
    x = num.text
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    but = browser.find_element_by_id("solve")
    but.click()

finally:
    time.sleep(999)
    browser.quit()
