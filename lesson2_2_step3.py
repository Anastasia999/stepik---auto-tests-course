from selenium import webdriver
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1_element = browser.find_element_by_id("num1")
    num1 = int(num1_element.text)
    num2_element = browser.find_element_by_id("num2")
    num2 = int(num2_element.text)
    answer = str(num2+num1)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_id("dropdown").send_keys(answer)

    submit = browser.find_element_by_class_name("btn.btn-default")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.quit()