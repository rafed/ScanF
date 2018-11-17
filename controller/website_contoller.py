from flask_restful import Resource, reqparse

from app import db
from model.website import Website

class WebsiteController(Resource):
    def get(self):
        websites = Website.query.all()
        return [x.as_dict() for x in websites] 

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('baseurl', required=True)
        parser.add_argument('title', required=True)

        args = parser.parse_args()
        
        baseurl = args['baseurl']
        title = args['title']
        
        website = Website(baseurl, title)
        website.save_to_db()
        return {"status":"ok"}

    def delete(self, id):
        website = Website.query.get(id)
        website.delete()
        return {"status":"ok"}
