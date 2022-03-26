from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num=browser.find_element_by_id('input_value')
    x=num.text
    y=calc(x)
    answer= browser.find_element_by_id('answer')
    answer.send_keys(y)
    #вариант прокрутки с использованием javascript
    '''button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()'''
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    _ =radio.location_once_scrolled_into_view
    radio.click()
    button = browser.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    '''Как вариант еще можно скрывать ненужный элемент
browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body
from selenium.webdriver.common.keys import Keys
browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх'''

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()