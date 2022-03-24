from selenium import webdriver
import time
import os


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    first_name=browser.find_element_by_tag_name("[name='firstname']")
    first_name.send_keys('Dzmitry')
    last_name=browser.find_element_by_tag_name("[name='lastname']")
    last_name.send_keys('Charnukha')
    email=browser.find_element_by_tag_name("[name='email']")
    email.send_keys('lambotik@mail.ru')
    load=browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    load.send_keys(file_path)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()