from selenium import webdriver
import math
def calc(x): return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_class_name("form-check-label")
    checkbox.click()

    radoibutton = browser.find_element_by_id("robotsRule")
    radoibutton.click()

    submit = browser.find_element_by_class_name("btn.btn-default")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.quit()