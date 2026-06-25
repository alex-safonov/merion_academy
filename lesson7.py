# Переход на Merion Academy

# Напишите скрипт, который выполняет следующие шаги:
# 1. Открыть браузер chrome
# 2. Перейти на страницу google.com
# 3. В строке поиска написать Merion Academy
# 4. Нажать Enter (Keys.RETURN)
# 5. На странице с результатами выбрать первую ссылку и кликнуть на нее
# 6. После перехода, получить текущий URL:
# - Если URL начинается со строки https://wiki.merionet.ru, написать Добро пожаловать в Merion Academy!.
# - Иначе написать в консоль Это другая ссылка.. 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://google.com")

driver.find_element(By.CSS_SELECTOR, "[name=q]").send_keys("Merion Academy" + Keys.RETURN)

# на странице с результатами
driver.find_element(By.CSS_SELECTOR, "h3").click()

# проверка, что мы на странице Merion Academy

if driver.current_url.startswith("https://wiki.merionet.ru"):
    print("Добро пожаловать в Merion Academy")
else:
    print("Это другая ссылка..")

driver.quit()