from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
messageField = driver.find_element(By.XPATH, '//*[@id="user-message"]')
messageField.send_keys('Hello World!')
showMessageButton = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
showMessageButton.click()

additionalField1 = driver.find_element(By.XPATH, '//*[@id="sum1"]')
additionalField1.send_keys('10')
additionalField2 = driver.find_element(By.XPATH, '//*[@id="sum2"]')
additionalField2.send_keys('25')
getTotalButton = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
getTotalButton.click()
