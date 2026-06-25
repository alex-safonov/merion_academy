# Форма авторизации

# Напишите скрипт, шаги:
# 1. Открыть страницу [http://the-internet.herokuapp.com/login](http://the-internet.herokuapp.com/login)
# 2. В поле uername ввести значение *`tomsmith`*
# 3. В поле password ввести значение *`SuperSecretPassword!`*
# 4. Нажмите кнопку Login
# 5. Выведите в консоль текст появившейся зеленой плашки

from selenium import webdriver
from selenium.webdriver.common.by import By

login = "tomsmith"
password = "SuperSecretPassword!"

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(login)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

flash = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(flash)

driver.quit()