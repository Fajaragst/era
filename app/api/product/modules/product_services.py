from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from app.api.product.models import Product
from app.api.product.models import db
from app.api.product.serializer import ProductSchema

from app.api.http_response import ok, created

from app.api.filter.sort import Sort

class ProductServices:

    @staticmethod
    def show(filter = {}):

        #find sqlalchemy order_by function by string from filter param (ex: Product.created_at.desc())     
        order_by = Sort(model=Product, order=filter.get('order'), field_name=filter.get('by')).get_sqlalchemy_sort_func()
        #pagination
        page = filter.get('page') or 1  
        limit = min( filter.get('limit') or 20 , 100) #set max limit 100

        #query
        products = Product.query.order_by(order_by).paginate(
            page= page, 
            per_page=limit, 
            error_out=False
        )

        #dump query result
        product_list = ProductSchema(many=True).dump(products.items)
        return ok(data= {
            "items" : product_list,
            "page" : products.page,
            "limit" : products.per_page,
            "total" : products.total
        })

    @staticmethod
    def add(product : Product):
        try:
            db.session.add(product)
            db.session.commit()
        except IntegrityError as error:
            db.session.rollback()
            print(error)
            #LOG HERE

        response = {
            "id" : product.id
        }

        return created(response)