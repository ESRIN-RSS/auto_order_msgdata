from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import re

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')

driver = webdriver.Chrome(options = options, executable_path='/usr/local/bin/chromedriver')

driver.get("https://eoportal.eumetsat.int/userMgmt/login.faces")
time.sleep(5)
driver.find_element_by_id("username").send_keys("")
driver.find_element_by_id ("password").send_keys("")
driver.find_element_by_name("submit").click()
time.sleep(3)
order_list = "//table"

driver.get("https://archive.eumetsat.int/usc/#os:")
time.sleep(5)
order_list_raw = driver.find_element_by_xpath(order_list).text
k = order_list_raw.split("\n")[2:]
chunks = [k[x:x+9] for x in range(0, len(k), 9)]
for c in chunks:
    if c[8] == "DELIVERED":
        print(c[0])
driver.quit()
