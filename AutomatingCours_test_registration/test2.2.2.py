from selenium import webdriver
import time

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    '''button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()'''
    #второй вариант
    button = browser.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view

    button.click()
    assert True


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.send_keys()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()