from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    # 1. Открыть страницу 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    # 2. Посчитать сумму заданных чисел
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    print(x)
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    print(y)
    z = int(x)+int(y)
    print(z)

    # 3. Выбрать в выпадающем списке значение равное расчитанной сумме
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(z)) # ищем элемент 


    # 4. Нажать кнопку "Submit"
    submitButton = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submitButton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# не забываем оставить пустую строку в конце файла



