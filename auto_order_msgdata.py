from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import argparse

parser = argparse.ArgumentParser(
    description="Auto order msg data slots.")
parser.add_argument("link", help="https://eoportal.eumetsat.int/ link to order.")
args = parser.parse_args()

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

def get_order_list():
    driver.get("https://archive.eumetsat.int/usc/#os:")
    time.sleep(5)
    order_list_raw = driver.find_element_by_xpath(order_list).text()
    print(order_list_raw)

# driver.get("https://archive.eumetsat.int/usc/#st:;id=EO:EUM:DAT:MSG:HRSEVIRI;delm=O;form=HRITTAR;band=1,2,3,4,5,6,7,8,9,10,11,12;subl=1,1,3712,3712;comp=NONE;med=NET;noti=1;satellite=MSG4,MSG2,MSG1,MSG3;ssbt=2020-01-05T00:00;ssst=2020-01-05T00:15;udsp=OPE;subSat=0;qqov=ALL;seev=0;smod=ALTHRV")
until = "(//input[@class=\"usc-TimeBox\"])[2]"
apply = "(//div[text()=\"Apply\"])[1]"
reset_times = "(//div[text()=\"Reset Times\"]/ancestor::*[position()=1])[1]"
next = "//div[text()=\"Next Step\"]"
chkout = "//div[text()=\"Go to Check Out\"]"
placeorder = "//div[text()=\"Place your Order\"]"
compression = "(//select[@class=\"gwt-ListBox\"])[1]"
order_list = "//table"

driver.get(args.link)
time.sleep(5)
driver.find_element_by_xpath(until).send_keys(Keys.RETURN)
driver.find_element_by_xpath(apply).click()
time.sleep(2)
driver.find_element_by_xpath(next).click()
time.sleep(2)
driver.find_element_by_xpath(next).click()
time.sleep(2)
driver.find_element_by_xpath(next).click()
time.sleep(2)
select = Select(driver.find_element_by_xpath(compression))
select.select_by_visible_text('GZIP')
time.sleep(2)
driver.find_element_by_xpath(chkout).click()
time.sleep(2)
driver.find_element_by_xpath(placeorder).click()
driver.quit()
