from flask import Blueprint, request
from marshmallow import ValidationError

from app.api.product.modules.product_services import ProductServices
from app.api.product.serializer import ProductSchema

from app.api.error.http import BadRequest

product_blueprint = Blueprint('product_blueprint', __name__,)

@product_blueprint.route('/product', methods=["GET"])
def show():
    #get filter param
    by = request.args.get("by", type=str) or ""
    order = request.args.get("order", type=str) or ""
    page = request.args.get("page", type=int) 
    limit = request.args.get("limit", type=int) 

    filter = {"by":by, "order":order, "limit" : limit, "page" : page }
    
    return ProductServices.show(filter=filter)


@product_blueprint.route('/product', methods=["POST"])
def add():

    #get request payload
    payload = request.json

    try:
        product = ProductSchema().load(payload)
    except ValidationError as e:
        raise BadRequest('INVALID PARAMETER', 'invalid parameter', e.messages)

    return ProductServices.add(product)
