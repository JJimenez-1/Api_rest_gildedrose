
from flask import Response, g
from flask_restful import fields, marshal_with, abort
# from repository.models import Item
from mongoengine.queryset.visitor import Q
from repository.db_atlas import get_db

from repository.repo import Factory


class Service():

    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }

    @staticmethod
    @marshal_with(resource_fields)
    def inventario():
        db = get_db()
        listaItems = []
        for item in g.Item.objects():
            listaItems.append(item)
        return listaItems

    @staticmethod
    @marshal_with(resource_fields)
    def getItem(itemName):
        db = get_db()
        items = g.Item.objects(name=itemName)
        if not items:
            abort(404, message="El item {} no existe".format(itemName))
        return list(items)

    @staticmethod
    def postItem(args):
        db = get_db()
        item = g.Item(name=args['name'])
        item.sell_in = args['sell_in']
        item.quality = args['quality']
        item.save()
