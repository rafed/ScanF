from flask_restful import Resource, reqparse

from app import db
from model.website import Website

from services.crawler import Crawler

crawler = Crawler()

class WebsiteController(Resource):
    def get(self):
        websites = Website.query.all()
        return [x.as_dict() for x in websites] 

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('url')
        parser.add_argument('stop')

        args = parser.parse_args()
        url = args['url']
        stop = args['stop']

        if stop is not None and stop is True:
            crawler.running = False
            return {
                "status":"ok",
                "msg":"Stopped crawler"
            }

        if crawler.running:
            return {
                "status":"ok",
                "msg":"busy"
            }, 403
        
        try:
            crawler.crawl(url)
        except:
            return {
                "status":"error",
                "msg":"bad url"
            }, 403
        
        return {"status":"ok"}

    def delete(self, id):
        website = Website.query.get(id)
        website.delete()
        return {"status":"ok"}
