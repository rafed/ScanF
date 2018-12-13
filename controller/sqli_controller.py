from flask_restful import Resource, reqparse

from app import db

from model.form import Form
from model.cookie import Cookie
from model.page import Page
from model.website import Website
from model.sql import SQLiStr

from services.auto_form_fill import AutoFormFill

import urllib.parse as urlparse
from urllib.parse import urlencode

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768")
chrome_options.add_argument("--headless")

class SQLiController(Resource):
    def get(self):
        sqls = SQLiStr.query.all()
        return [x.as_dict() for x in sqls] 


class AutoSQLAttack(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('form_id')
        parser.add_argument('payload')

        args = parser.parse_args()
        form_id = args['form_id']
        payload = args['payload']

        form = Form.query.filter(Form.id == form_id).first()
        fields = AutoFormFill.fillForm(form_id)

        # Get the cookies
        page = Page.query.filter(Page.id == form.page_id).first()
        website =  Website.query.filter(Website.id == page.website_id).first()
        cookies = Cookie.query.filter(Cookie.website_id == website.id).all()

        # Load page once to setup browser
        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
        driver.get(form.form_action)
        for cookie in cookies:
            cookie_dict = {'name': cookie.name, 'value': cookie.value}
            print("done upto", cookie_dict)
            driver.add_cookie(cookie_dict)

        # print("The url", urlencode(fields))

        if form.method == 'get':
            url_parts = list(urlparse.urlparse(form.form_action))
            query = dict(urlparse.parse_qsl(url_parts[4]))
            query.update(fields)

            url_parts[4] = urlencode(query)
            url = urlparse.urlunparse(url_parts)

            driver.get(url)
            # img_path =  'store/'+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+'.png'
            # driver.save_screenshot(img_path)
        elif form.method == 'post':
            url_parts = list(urlparse.urlparse(form.form_action))
            query = dict(urlparse.parse_qsl(url_parts[4]))
            query.update(fields)

            url_parts[4] = urlencode(query)
            print("woow", urlparse.urlunparse(url_parts))

            pass

        driver.quit()
        print(fields, payload)
        return {'status':'ok'}
