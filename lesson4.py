# Модальное окно

#Напишите скрипт. Шаги:
# 1. Открыть страницу[http://the-internet.herokuapp.com/entry_ad](http://the-internet.herokuapp.com/entry_ad) ;
# 2. В модальном окне нажать на кнопку Сlose
# 3. Выведите в консоль текст элемента с id = content
# >Подсказка: тут вам может понадобиться time.sleep(3)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")

time.sleep(3)

close = driver.find_element(By.CSS_SELECTOR, "#modal .modal-footer")

close.click()

content = driver.find_element(By.CSS_SELECTOR, "#content").text
print(content)

driver.quit()