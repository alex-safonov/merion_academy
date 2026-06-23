# Клик по кнопке с css-классом

# Напишите скрипт. Шаги: 
# 1. Открыть страницу http://uitestingplayground.com/classattr
# 2. Кликнуть на синюю(!) кнопку
# 3. Запустите скрипт 3 раза. Убедитесь, что код не требуется редактировать – скрипт всегда работает. 


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

btn.click()

driver.quit()