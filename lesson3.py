from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

btn.click()

driver.quit()