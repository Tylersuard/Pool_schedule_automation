#1. Navigate to www.ciymca.org/pool
#1.2 click next day button xpath: /html/body/div[1]/div/div[4]/main/div/div/div[2]/div[2]/article/div[2]/div[4]/div/div/div[3]/div[1]/div/h2/button[2]
#2. Click 4:00 button xpath: /html/body/div[1]/div/div[4]/main/div/div/div[2]/div[2]/article/div[2]/div[4]/div/div/div[3]/div[2]/div[1]/div/div[21]/div[6]/div/a
#3. Enter username xpath: //*[@id="login"]
#4. Enter password xpath: //*[@id="password"]
#5. Click login button xpath: /html/body/div/div[2]/div/div/form/fieldset/div[3]/input
#6. Click reserve a spot xpath: /html/body/div/div[2]/div/div/form/fieldset/div/input[4]

import time
from datetime import date, timedelta
import datetime

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains


url = 'https://www.ciymca.org/pool'

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
print("driver loaded, getting url")
driver.get(url)
print("url gotted")
time.sleep(1)


click_next_day_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/main/div/div/div[2]/div[2]/article/div[2]/div[4]/div/div/div[3]/div[1]/div/h2/button[2]').click()
click_400_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/main/div/div/div[2]/div[2]/article/div[2]/div[4]/div/div/div[3]/div[2]/div[1]/div/div[21]/div[6]/div/a').click()

time.sleep(1)

username = driver.find_element_by_xpath('//*[@id="login"]')
username.send_keys("")
time.sleep(.5)

password = driver.find_element_by_xpath('//*[@id="password"]')
username.send_keys("")
time.sleep(1)

click_login = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/fieldset/div[3]/input').click()
click_reserve = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/form/fieldset/div/input[4]').click()




"""

username = driver.find_element_by_id("user_email")
username.clear()
username.send_keys("myname@email.com")

time.sleep(1)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("P@$$w0rd")

time.sleep(1)

sign_in_submit_form = driver.find_element_by_css_selector('div.bs-form-group:nth-child(4) > button:nth-child(1)').click()
