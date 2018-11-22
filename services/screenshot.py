
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768")
chrome_options.add_argument("--headless")

class Screenshot:
    @staticmethod
    def snap(url):
        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
        driver.get(url)
        img_path =  'store/'+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+'.png'
        driver.save_screenshot(img_path)
        driver.quit()
        return img_path