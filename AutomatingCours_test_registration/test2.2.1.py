from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1=browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    num3=num1.text
    num4=num2.text
    sum=int(num3)+int((num4))
    sum1=str(sum)
    select = browser.find_element_by_id('dropdown').click()
    answer=browser.find_element_by_css_selector(f"[value='{sum1}']").click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()