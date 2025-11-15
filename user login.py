import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
time.sleep(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#driver.find_element(By.NAME,"username").send_keys("admin")
#driver.find_element(By.NAME,"password").send_keys("admin 123")
#driver.find_element(By.LINK_TEXT,"login").click()
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,"input[type=checkbox]").click()
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("admin 123")
driver.find_element(By.LINK_TEXT,"Login").click()