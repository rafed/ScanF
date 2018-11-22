from flask_restful import Resource, reqparse

from app import db
from model.page import Page

class PageScreenshotController(Resource):
    def get(self, id):
        page = Page.query.filter(Page.id == id)
        if page.screenshot_path is None:
            pass
            ### GET SCREENSHOT

    def delete(self, id):
        page = Page.query.get(id)
        page.delete()
        return {"status":"ok"}
