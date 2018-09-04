#!usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768");
# chrome_options.add_argument("--start-maximized") # doesnt work for headless, go with window-size
chrome_options.add_argument("--headless")  


driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

driver.get('http://www.google.com/');
time.sleep(1) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('Rafed Yasir')
# search_box.submit()
# time.sleep(2) # Let the user actually see something!

driver.save_screenshot('shot.png')

# html = driver.page_source
html = driver.execute_script("return document.body.innerHTML")

print(html)

driver.quit()