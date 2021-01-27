from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.set_script_timeout(10)
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
time.sleep(2)
print(driver.title)
assert "Register" in driver.current_url

time.sleep(2)

s = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/a")
f = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/a")
y = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a")

act = ActionChains(driver)
act.move_to_element(s).move_to_element(f).move_to_element(y).click().perform()


