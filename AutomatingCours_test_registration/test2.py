from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    case=browser.find_element_by_id('treasure')
    case_atribute=case.get_attribute('valuex')
    x=case_atribute
    print(x)
    y= calc(x)
    print(y)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio=browser.find_element_by_id('robotsRule')
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(999)
    # закрываем браузер после всех манипуляций
    browser.quit()