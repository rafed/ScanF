from flask_restful import Resource, reqparse

from app import db
from model.cookie import Cookie

class CookieController(Resource):
    def get(self, id):
        cookies = Cookie.query.filter(Cookie.website_id==id).all()
        return [x.as_dict() for x in cookies] 

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('name')
        parser.add_argument('value')

        args = parser.parse_args()
        id = args['id']
        name = args['name']
        value = args['value']

        cookie = Cookie(id, name, value)
        cookie.save_to_db()

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('name')
        parser.add_argument('value')

        args = parser.parse_args()
        id = args['id']
        name = args['name']
        value = args['value']

        cookie = Cookie.query.get(id)
        cookie.name = name
        cookie.value = value
        cookie.update()
        
        return {"status":"ok"}

    def delete(self, id):
        cookie = Cookie.query.get(id)
        cookie.delete()
        return {"status":"ok"}
