from app import app, api
from flask import send_from_directory

from controller.website_contoller import WebsiteController
from controller.cookie_contoller import CookieController
from controller.page_contoller import PageController
from controller.screenshot_controller import PageScreenshotController
from controller.form_contoller import FormController
from controller.field_contoller import FieldController
from controller.test_controller import TestController

from controller.sqli_controller import SQLiController, AutoSQLAttack, ManualSQLAttack
from controller.xss_controller import XssController, AutoXSSAttack

############# Static files ###############

@app.route('/')
@app.route('/index')
def serve_index():
    return send_from_directory('client/', 'index.html')

@app.route('/<path:path>')
def serve_web_client(path):
    return send_from_directory('client', path)

@app.route('/store/<path:path>')
def serve_stores(path):
    return send_from_directory('store', path)

############ API ###############

api.add_resource(WebsiteController, '/website', '/website/<string:id>')

api.add_resource(CookieController, '/cookie', '/cookie/<string:id>')

api.add_resource(PageController, '/page/<string:id>')

api.add_resource(PageScreenshotController, '/page_screenshot/<string:id>')

api.add_resource(FormController, '/form/<string:id>')

api.add_resource(FieldController, '/field/<string:id>')

api.add_resource(TestController, '/test', '/test/<string:form_id>')

api.add_resource(SQLiController, '/sql')
api.add_resource(AutoSQLAttack, '/autosqlattack')
api.add_resource(ManualSQLAttack, '/manualsqlattack')

api.add_resource(XssController, '/xss')
api.add_resource(AutoXSSAttack, '/autoxssattack')
