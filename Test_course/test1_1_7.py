from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # общее количетсво доступных полей ввода
    spLabel=browser.find_elements_by_xpath("//div//label")
    newlist=[]
    list=[]
    #Получаем список с названиями полей для заполнения
    for sp in spLabel:
        newlist.append(sp.text)
    #Проверяем наличие обязательных полей для заполнения проверкой на наличие * в элементе полученого списка
    for i in range(len(spLabel)):
        if '*' in newlist[i]:
            list.append(newlist[i]) #Получаем список в конкретном случае это:['First name*', 'Last name*', 'Email*']
    inp1=newlist[0]
    inp2=newlist[1]
    inp3=newlist[2]
    # Ваш код, который заполняет обязательные поля
    input1=browser.find_element_by_xpath("//*[@placeholder='Input your first name']")
    input1.send_keys('Dzmitry')
    input2 = browser.find_element_by_xpath("//*[@placeholder='Input your last name']")
    input2.send_keys('Charnukha')
    input3 = browser.find_element_by_xpath("//*[@placeholder='Input your email']")
    input3.send_keys('lambotik@mail.ru')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()