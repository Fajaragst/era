from flask_marshmallow  import Marshmallow
from marshmallow import fields, post_load, validate

from app.api.product.models import Product

ma = Marshmallow()

class ProductSchema(ma.Schema):
    """This is class Schema for Product"""
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=255))
    description = fields.Str(allow_none=True, load_default=None, validate=validate.Length(max=510))
    price = fields.Number(required=True, validate=validate.Range(min=0))
    quantity = fields.Int(required=True, validate=validate.Range(min=0))

    @post_load
    def make_object(self, request_data,**kwargs):
        """ create product object """
        return Product(**request_data)
    