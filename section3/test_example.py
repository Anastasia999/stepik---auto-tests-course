from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input.form-control.first:required")
        input1.send_keys("Anastasiya")
        input2 = browser.find_element_by_css_selector("input.form-control.second:required")
        input2.send_keys("Leonovich")
        input3 = browser.find_element_by_css_selector("input.form-control.third:required")
        input3.send_keys("la+1@mail.com")

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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You haven't successfully registered!1")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input.form-control.first:required")
        input1.send_keys("Anastasiya")
        input2 = browser.find_element_by_css_selector("input.form-control.second:required")
        input2.send_keys("Leonovich")
        input3 = browser.find_element_by_css_selector("input.form-control.third:required")
        input3.send_keys("la+1@mail.com")

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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You haven't successfully registered!2")


if __name__ == "__main__":
    unittest.main()