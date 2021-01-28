from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
time.sleep(1)

a = driver.find_elements(By.TAG_NAME,"a")
print(len(a))
for i in a:
    print(i.text)

forsignin = driver.find_element_by_xpath("//*[@id='nav-link-accountList']/span[1]")
signin = driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span")

action = ActionChains(driver)
action.move_to_element(forsignin).move_to_element(signin).click().perform()
print(driver.current_url)

driver.find_element_by_xpath("//input[@id = 'continue']").is_enabled()
driver.find_element_by_xpath("//input[@id = 'continue']").is_displayed()
driver.find_element_by_xpath("//input[@id = 'continue']").click()

driver.find_element_by_xpath("//*[@id='auth-email-missing-alert']/div/div").is_displayed()
time.sleep(2)
driver.back()

all = driver.find_element_by_xpath("//*[@id='searchDropdownBox']")

drp = Select(all)

drp.select_by_index(2)
time.sleep(3)
drp.select_by_value("search-alias=nowstore")
time.sleep(3)
drp.select_by_visible_text("Apps & Games")
time.sleep(3)

driver.get("https://www.youtube.com/")
time.sleep(5)

window = driver.window_handles

for w in window:
    driver.switch_to.window(w)
    print(driver.title)
    if driver.title == "YouTube":
        driver.quit()

print("Task Completed")