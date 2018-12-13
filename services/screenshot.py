
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime

from model.website import Website
from model.cookie import Cookie

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768")
chrome_options.add_argument("--headless")

class Screenshot:
    @staticmethod
    def snap(page):
        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)

        website = Website.query.filter(Website.id == page.website_id).first()
        cookies = Cookie.query.filter(Cookie.website_id == website.id).all()

        driver.get('http://'+website.baseurl+'/this404.html')

        for cookie in cookies:
            cookie_dict = {'name': cookie.name, 'value': cookie.value}
            driver.add_cookie(cookie_dict)

        driver.get(page.url)
        img_path =  'store/'+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+'.png'
        driver.save_screenshot(img_path)
        driver.quit()
        return img_path