from flask_restful import Resource, reqparse

from app import db
from model.page import Page

class PageController(Resource):
    def get(self, website_id):
        pages = Page.query.filter(Page.website_id == website_id)
        return [x.as_dict() for x in pages] 

    def delete(self, id):
        page = Page.query.get(id)
        page.delete()
        return {"status":"ok"}
