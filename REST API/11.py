from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/search?hl=en&sxsrf=ALeKk02C0eySZD16uolcRcmk_hqlXP-JEQ%3A1611553330549&source=hp&ei=MloOYNTmHvGe4-EPt6ywoAM&q=mobile&oq=mobile&gs_lcp=CgZwc3ktYWIQDDIECCMQJzILCAAQsQMQgwEQkQIyBQgAEJECMgUIABCxAzICCAAyBQgAELEDMgIIADICCAAyBQgAELEDMgIIADoKCC4QxwEQowIQJzoHCAAQyQMQQzoECAAQQzoHCAAQsQMQQzoKCC4QxwEQowIQQzoICAAQsQMQgwE6CAguELEDEIMBUL8WWPEgYLNlaABwAHgAgAGJAYgBjwaSAQMwLjaYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjUx7T-r7buAhVxzzgGHTcWDDQQ4dUDCAs")

driver.implicitly_wait(10)

link = driver.find_elements(By.TAG_NAME,"a")

for i in link:
    c = driver.find_elements_by_xpath("//*[@id='rso']/div["+str(i)+"]/div/div[1]/a/h3/span")
    print(c.text)
    i = i + 1



