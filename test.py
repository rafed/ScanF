#!usr/bin/python3

import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

driver.get('http://www.google.com/');
time.sleep(2) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Rafed Yasir')
search_box.submit()
time.sleep(2) # Let the user actually see something!

driver.quit()