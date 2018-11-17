from app import api

from controller.test_controller import TestController

api.add_resource(TestController, '/test', '/test/<string:form_id>')
