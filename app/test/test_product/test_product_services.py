import pytest 

from app.api.product.modules.product_services import ProductServices
from app.api.product.models import Product

from app.test.test_app import TestApp

class TestProductServices(TestApp):

    DEFAULT_PRODUCT_DATA = {
        "name" : "Apple MacBook Air M2 (2022)",
        "description" : "Bertenaga super berkat chip M2 generasi berikutnya, MacBook Air yang didesain ulang menggabungkan performa andal dengan kekuatan baterai hingga 18 jam ke dalam penutup berbahan aluminium yang luar biasa tipis.",
        "quantity" : 10,
        "price" : 19999000
    }

    def _create_product(self, data=DEFAULT_PRODUCT_DATA):

        product = ProductServices.add(Product(**data))

        product_id = product[0]["data"]["id"]
        response = {
            "object" : product,
            "id" : product_id,
        }
        
        return response

    def _create_multiple_products(self, data=DEFAULT_PRODUCT_DATA, total=10):

        products = []
        #seed product with diferent price
        for i in range(total):
            product = {
                "name" : data['name'] + str(i),
                "description" : data['description'] + str(i),
                "price" : data['price'] + i,
                "quantity" : data['quantity'] + i
            }
            response = self._create_product(product)
            products.append(products)

        response = {
            "objects" : products,

        }
        
        return response


    def test_add(self):
        """ test function that adding product"""
        response = self._create_product()
        assert response["object"]
        assert response["id"] == 1

    def test_show_all(self):
        """ test function that show all product"""
        response = self._create_product()
        result = ProductServices.show()

        assert len(result[0]["data"]["items"]) == 1


    @pytest.mark.parametrize("by,order,sort_reverse", [
        ("price", "desc", True),
        ("price", "asc", False),
        ("name", "desc", True),
        ("name", "asc", False),
        ("created_at", "desc", True)
    ])
    def test_show_all_with_sort(self, by, order, sort_reverse):
        """ test function that show all product with diferent parameter"""

        self._create_multiple_products()

        filter = {"by" : by, "order" : order}
        result = ProductServices.show(filter)

        assert sorted(result[0]["data"]["items"], key = lambda x : x[by], reverse=sort_reverse) == result[0]["data"]["items"]
