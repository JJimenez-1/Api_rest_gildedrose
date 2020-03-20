from flask_restful import Resource, Api, reqparse
from repository.models import Item
from services.service import Service


class Items(Resource):

    def get(self, itemName):
        return Service.getItem(itemName), 200

    def post(self):
        args = self.parseRequest()
        Service.postItem(args)
        return '', 201

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='name required')
        parser.add_argument('sell_in', type=int, required=True,
                            help='sellin required')
        parser.add_argument('quality', type=int, required=True,
                            help='quality required')
        return parser.parse_args()

    def delete(self):
        args = self.parseRequest()
        Service.deleteItem(args)
        return '', 204
