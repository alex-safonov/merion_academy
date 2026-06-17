# Клик по кнопке

# Напишите скрипт. Шаги:
# 1. Открыть страницу http://the-internet.herokuapp.com/add_remove_elements/
# 2. 5 раз кликнуть на кнопку Add Element
# 3. Собрать со страницы список кнопок Delete
# 4. Вывести на экран размер списка

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

btn = driver.find_element(By.CSS_SELECTOR, "button")

btn.click()
btn.click()
btn.click()
btn.click()
btn.click()

delete_buttons = driver.find_element(By.CSS_SELECTOR, "#elements").find_elements(By.CSS_SELECTOR, "button")

print(len(delete_buttons))

driver.quit()
