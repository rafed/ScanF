from app import api

from controller.website_contoller import WebsiteController

api.add_resource(WebsiteController, '/website')
