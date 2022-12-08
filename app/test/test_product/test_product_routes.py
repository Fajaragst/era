import json
import pytest

from app.test.test_base_routes import BaseTestRoutes
from app.test.test_app import BASE_URL

class TestProductRoutes(BaseTestRoutes):

    DEFAULT_PRODUCT_DATA = {
        "name" : "Apple MacBook Air M2 (2022)",
        "description" : "Bertenaga super berkat chip M2 generasi berikutnya, MacBook Air yang didesain ulang menggabungkan performa andal dengan kekuatan baterai hingga 18 jam ke dalam penutup berbahan aluminium yang luar biasa tipis.",
        "quantity" : 10,
        "price" : 19999000
    }


    def show_all_product(self, query_param = "?"):
        url = BASE_URL + "/product" + query_param
        result = self.show(url=url)
        return result

    def add_product(self, data=DEFAULT_PRODUCT_DATA):
        params = data
        url = BASE_URL + "/product"
        result = self.add(params=params, url=url)
        return result

    def test_show_all_product(self):
        result = self.show_all_product()
        assert result.status_code == 200

    def test_add_product(self):
        result = self.add_product()

        assert result.status_code == 201

    def test_add_show_all_product(self):

        self.add_product()

        result = self.show_all_product()
        assert result.status_code == 200
