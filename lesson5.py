# Поле ввода

# Напишите скрипт. Шаги:
# 1. http://the-internet.herokuapp.com/inputs
# 2. Введите в поле текст 1000
# 3. Очистите это поле (метод `clear`)
# 4. введите в это же поле текст 2000

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.CSS_SELECTOR, "input")

input.send_keys("1000")
input.clear()
input.send_keys("2000")

driver.quit()