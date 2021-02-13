from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

act = ActionChains(driver)

driver.set_page_load_timeout(15)
driver.set_script_timeout(2)
driver.get("https://www.google.in/")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(1)

driver.find_element_by_xpath("//input[@class = 'gLFyf gsfi']").send_keys("Mobile")
act.send_keys(Keys.ENTER).perform()

links = driver.find_elements_by_xpath("//h3[@class = 'LC20lb DKV0Md']")

print(len(links))

for i in links:
    print(i.text)

driver.close()


