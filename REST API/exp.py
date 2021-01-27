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

f_name = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[1]/input")
l_name = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[2]/input")
address = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[2]/div/textarea")
email = driver.find_element_by_xpath("//*[@id='eid']/input")
ph = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[4]/div/input")
male = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[1]")
female = driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[5]/div/label[2]")
cricket = driver.find_element_by_id("checkbox1")
upload = driver.find_element_by_xpath("//*[@id='imagesrc']")
skill = driver.find_element_by_id("Skills")
lan = driver.find_element_by_id("msdd")

driver.implicitly_wait(5)

f_name.is_displayed()
l_name.is_displayed()
female.is_enabled()

f_name.send_keys("Ayan")
l_name.send_keys("Dutta")
address.send_keys("Global Tech park front gate")
email.send_keys("ayand777@gmail.com")
ph.send_keys("9674522538")
male.click()
male.is_selected()
cricket.click()
cricket.is_selected()
upload.send_keys("C:/Users/Ayan Dutta/Pictures/Saved Pictures/screen-3.jpg")

drp = Select(skill)
drp.select_by_value("Adobe InDesign")
time.sleep(2)
drp.select_by_visible_text("C")
time.sleep(2)
drp.select_by_index(6)
time.sleep(2)
lan.click()
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li[6]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[7]/div/multi-select/div[2]/ul/li[8]/a").click()
fb = driver.find_element_by_xpath("//*[@id='footer']/div/div/div[2]/a[1]")
s = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/a")
f = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[3]/a")


#act = ActionChains(driver)
#act.move_to_element(s).move_to_element(f).click().perform()

time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();", fb)
fb.click()
time.sleep(5)
print(driver.current_url)
driver.quit()
