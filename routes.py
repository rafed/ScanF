from app import app, api
from flask import send_from_directory

from controller.website_contoller import WebsiteController
from controller.test_controller import TestController
from controller.page_contoller import PageController


############# Static files ###############

@app.route('/')
@app.route('/index')
def serve_index():
    return send_from_directory('client/', 'index.html')

@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory('client', path)

############ API ###############

api.add_resource(WebsiteController, '/website')

api.add_resource(TestController, '/test', '/test/<string:form_id>')

api.add_resource(PageController, '/page/<string:website_id>')
