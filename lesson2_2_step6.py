from selenium import webdriver
import math
import ChromeOptions
def calc(x): return str(math.log(abs(12 * math.sin(int(x)))))
options = ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
link = "http://suninjuly.github.io/execute_script.html"

browser.get(link)
x_element = browser.find_element_by_id("input_value")


x = int(x_element.text)
print(x)
y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)

option1 = browser.find_element_by_class_name("form-check-label")
option1.click()

option2 = browser.find_element_by_class_name("form-check-label")
#browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#assert True