from selenium import webdriver


website = 'https://openweathermap.org/city/5206379'


driver = webdriver.Chrome()
driver.get(website)

driver.quit()





