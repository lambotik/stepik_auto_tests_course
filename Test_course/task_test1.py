import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test_login:
    sp_text=''
    @pytest.mark.parametrize('links',
                             ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                              'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                              'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                              'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
    def test(self,browser,links):
        sp=''
        wait = WebDriverWait(browser, 10)
        link=f'{links}'
        answer = math.log(int(time.time()))
        browser.get(link)
        question=browser.find_element(By.XPATH,"//*[@placeholder='Напишите ваш ответ здесь...']")
        question.send_keys(answer)
        button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@class="submit-submission"]')))
        button.click()
        answer1 = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
        x = answer1.text
        if x!="Correct!":
            sp+=x
        assert "Correct!" in x

        if __name__ == "__main__":
            pytest.main()






