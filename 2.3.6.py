from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

try:
    # 1. Открыть страницу 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # 2. Нажать на кнопку
    submitButton = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submitButton.click()

    # 3. Переключиться на новую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    input = browser.find_element(By.ID, "input_value")
    num = input.text
    x = int(num)
    def calc(x):
        return math.log(abs(12*math.sin(x)))
    y = calc(x)
    output = browser.find_element(By.ID, "answer")
    output.send_keys(y)
    submitButton = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submitButton.click()
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла



