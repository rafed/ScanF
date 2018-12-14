from flask_restful import Resource, reqparse

from app import db

from model.form import Form
from model.cookie import Cookie
from model.page import Page
from model.website import Website
from model.sql import SQLiStr
from model.test import Test

from services.auto_form_fill import AutoFormFill

import urllib.parse as urlparse
from urllib.parse import urlencode

import re
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("window-size=1366,768")
chrome_options.add_argument("--headless")

errors = [
    'You have an error in your SQL syntax;',
    'Warning: mysql_fetch_array() expects parameter'
    ' - You have an error in your SQL syntax; check the manual that corresponds to your',
    'Unclosed quotation mark after the character',
    'quoted string not properly terminated'
]

script = '''
function post(path, params) {
    method = "post"; 

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}
'''

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

        # Load page once to setup browser and add cookies
        driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
        driver.get(form.form_action)
        for cookie in cookies:
            cookie_dict = {'name': cookie.name, 'value': cookie.value}
            print("done upto", cookie_dict)
            driver.add_cookie(cookie_dict)

        # set payloads
        for k, v in fields.items():
            temp_fields = fields.copy()
            temp_fields[k] = payload

            print("Form is of type", form.method)
            if form.method == 'get':
                url_parts = list(urlparse.urlparse(form.form_action))
                query = dict(urlparse.parse_qsl(url_parts[4]))
                query.update(temp_fields)

                url_parts[4] = urlencode(query)
                url = urlparse.urlunparse(url_parts)

                start_time = time.time()
                driver.get(url)
                duration = time.time() - start_time
                
            elif form.method == 'post':
                script_post = 'post("{}", data={});'.format(form.form_action, json.dumps(temp_fields))
                attack_script = script + script_post

                start_time = time.time()
                driver.execute_script(attack_script)
                duration = time.time() - start_time

            # DO TEST STUFF
            page = driver.page_source
            file_path = 'store/'+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+'.html'
            file_ = open(file_path, 'w')
            file_.write(page)
            file_.close()

            img_path =  'store/'+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+'.png'
            driver.save_screenshot(img_path)

            date_now = datetime.now() #.strftime("%d-%m-%Y %H:%M:%S")

            vulnerable = 'not vulnerable'
            if 'sleep' in payload:
                if duration > 7:
                    vulnerable = 'vulnerable'
            else:
                for error in errors:
                    if bool(re.search(error, page)):
                        vulnerable = 'vulnerable'
                        break

            test = Test(form_id, 'sql', json.dumps(temp_fields), file_path, img_path, date_now, duration, vulnerable)
            test.save_to_db()

        driver.quit()
        return {'status':'ok'}
