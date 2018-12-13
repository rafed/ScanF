from flask_restful import Resource, reqparse

from app import db
from model.page import Page

from services.screenshot import Screenshot

class PageScreenshotController(Resource):
    def get(self, id):
        page = Page.query.get(id)
        
        if page.screenshot_path is None:
            img_path = Screenshot.snap(page)
            page.screenshot_path = img_path
            page.update()

        return page.as_dict()
