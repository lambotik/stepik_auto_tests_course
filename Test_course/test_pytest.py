import unittest
import pytest
from typing import List


from selenium import webdriver
import time

from selenium.webdriver.remote.webelement import WebElement


class RegistrationTest(unittest.TestCase):
    def test1_1_6(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        spLabel = browser.find_elements_by_xpath("//div//label")
        newlist = []
        list = []
        # Получаем список с названиями полей для заполнения
        for sp in spLabel:
            newlist.append(sp.text)
        # Проверяем наличие обязательных полей для заполнения проверкой на наличие * в элементе полученого списка
        for i in range(len(spLabel)):
            if '*' in newlist[i]:
                list.append(newlist[i])  # Получаем список в конкретном случае это:['First name*', 'Last name*', 'Email*']
        inp1 = newlist[0]
        inp2 = newlist[1]
        inp3 = newlist[2]
        input1 = browser.find_element_by_xpath("//*[@placeholder='Input your first name']")
        input1.send_keys('Dzmitry')
        input2 = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
        input2.send_keys('Charnukha')
        input3 = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
        input3.send_keys('lambotik@mail.ru')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        answer=browser.find_element_by_xpath('//h1')
        ans=answer.text
        self.assertEqual("Congratulations! You have successfully registered!",f'{ans}')

    def test1_1_7(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        spLabel = browser.find_elements_by_xpath("//div//label")
        newlist = []
        list = []
        for sp in spLabel:
            newlist.append(sp.text)
        for i in range(len(spLabel)):
            if '*' in newlist[i]:
                list.append(
                    newlist[i])
        input1 = browser.find_element_by_xpath("//*[@placeholder='Input your first name']")
        input1.send_keys('Dzmitry')
        input2 = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
        input2.send_keys('Charnukha')
        input3 = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
        input3.send_keys('lambotik@mail.ru')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        answer = browser.find_element_by_xpath('//h1')
        ans = answer.text
        self.assertEqual("Congratulations! You have successfully registered!", f'{ans}')


if __name__ == "__main__":
    unittest.main()