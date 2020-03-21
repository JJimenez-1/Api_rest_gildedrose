from flask_restful import Resource, Api
# from repository.models import Item
from services.service import Service


class SellIn(Resource):
    def get(self, itemSellIn):
        return Service.filterSell_in(itemSellIn), 200
