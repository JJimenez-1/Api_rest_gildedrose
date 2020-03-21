from flask_restful import Resource, Api
# from repository.models import Item
from services.service import Service

class Sell_in(Resource):
    def get(self, itemSell_in):
        return Service.filterSell_in(itemSell_in), 200