
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

class Screenshot:
    @staticmethod
    def snap(url):
        driver.get(url)
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        driver.save_screenshot('store/'+date+'.png')
        # driver.quit()