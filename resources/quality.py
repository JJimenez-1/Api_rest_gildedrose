from flask_restful import Resource, Api
# from repository.models import Item
from services.service import Service

class Quality(Resource):
    def get(self, itemQuality):
        return Service.filterQuality(itemQuality), 200

